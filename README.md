Project Andvari - linked data application
=========================================

This application will allow for users to apply tags from an RDF ontology to images from several different data sets
for the multi-institutional collaboration known as Project Andvari.

This application has three main files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.

Adding data
===========

Data for this application will be imported from a csv file, and has a simple structure:

* Object URI
* Object image link
* Image licence terms
* Label chosen by project Andvari team

**NOTE**: This application uses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify
the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).

Institutional partners
======================
[![The Project Andvari logo](https://projectandvari.files.wordpress.com/2014/03/project_andvari_logo-for-wordpress-1.jpg)](http://andvari.org)
[![The British Museum logo](/static/img/bmBlackWhite.png)](http://britishmuseum.org)
[![The Portable Antiquities Scheme logo](https://finds.org.uk/assets/logos/pas.jpg)](https://finds.org.uk)

Funded by:
==========
[![National Endowment for the Humanities logo](http://www.andvari.org/images/NEHlogo.jpg)](http://www.neh.gov/)


