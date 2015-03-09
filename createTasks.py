#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import json
from optparse import OptionParser
import pbclient
import random
import logging
from requests import exceptions
from time import sleep


def contents(filename):
    return file(filename).read()


def handle_arguments():
    # Arguments for the application
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    # URL where PyBossa listens
    parser.add_option("-s", "--server", dest="api_url",
                      help="PyBossa URL http://domain.com/", metavar="URL",
                      default="http://localhost:5000/")
    # API-KEY
    parser.add_option("-k", "--api-key", dest="api_key",
                      help="PyBossa User API-KEY to interact with PyBossa",
                      metavar="API-KEY")
    # Create App
    parser.add_option("-c", "--create-app", action="store_true",
                      dest="create_app",
                      help="Create the application",
                      metavar="CREATE-APP")

    # Update template for tasks and long_description for app
    parser.add_option("-t", "--update-template", action="store_true",
                      dest="update_template",
                      help="Update Tasks template",
                      metavar="UPDATE-TEMPLATE")

    # Modify the number of TaskRuns per Task
    # (default 30)
    parser.add_option("-n", "--number-answers",
                      type="int",
                      dest="n_answers",
                      help="Number of answers per task",
                      metavar="N-ANSWERS",
                      default=3)

    parser.add_option("-a", "--application-config",
                      dest="app_config",
                      help="Application config file",
                      metavar="APP-CONFIG",
                      default="app.json")

    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
    (options, args) = parser.parse_args()

    if not options.create_app and not options.update_template:
        parser.error("Please check --help or -h for the available options")

    if not options.api_key:
        parser.error("You must supply an API-KEY to create an \
                      application and tasks in PyBossa")

    return options


def get_configuration():
    options = handle_arguments()

    # Load app details
    try:
        with file(options.app_config) as app_json:
            app_config = json.load(app_json)
    except IOError:
        print "Application config file is missing! Please create a new one"
        exit(1)

    return (app_config, options)


def run(app_config, options):

    def check_api_error(api_response):
        """Check if returned API response contains an error"""
        if type(api_response) == dict and (api_response.get('status') == 'failed'):
            raise exceptions.HTTPError

    def format_error(module, error):
        """Format the error for the given module"""
        logging.error(module)
        # Beautify JSON error
        if type(error) == list:
            print "Application not found"
        else:
            print json.dumps(error, sort_keys=True, indent=4, separators=(',', ': '))
        exit(1)

    def find_app_by_short_name():
        try:
            response = pbclient.find_app(short_name=app_config['short_name'])
            check_api_error(response)
            return response[0]
        except:
            format_error("pbclient.find_app", response)

    def setup_app():
        app = find_app_by_short_name()
        app.long_description = contents('long_description.html')
        app.info['task_presenter'] = contents('template.html')
        app.info['thumbnail'] = app_config['thumbnail']
        app.info['tutorial'] = contents('tutorial.html')

        try:
            response = pbclient.update_app(app)
            check_api_error(response)
            return app
        except:
            format_error("pbclient.update_app", response)

    pbclient.set('api_key', options.api_key)
    pbclient.set('endpoint', options.api_url)

    if options.verbose:
        print('Running against PyBosssa instance at: %s' % options.api_url)
        print('Using API-KEY: %s' % options.api_key)


    if options.update_template:
        print "Updating app template"
        # discard return value
        setup_app()

if __name__ == "__main__":
    app_config, options = get_configuration()
