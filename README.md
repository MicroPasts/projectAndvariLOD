Project Andvari - linked data application
=========================================

This application will allow for users to apply tags from an RDF ontology to images from several different data sets
for the multi-institutional collaboration known as Project Andvari.

This application has three main files:

*  createTasks.py: for creating the application in PyBossa. Tasks will be imported from a CSV.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.

Adding data
===========

Data for this application will be imported from a csv file, and has a simple structure:

* Object URI
* Object image link
* Label chosen by project Andvari team
* n_answers - the default redundancy of the app

**NOTE**: This application uses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify
the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).

Institutional partners
======================
[![The Project Andvari logo](https://projectandvari.files.wordpress.com/2014/03/project_andvari_logo-for-wordpress-1.jpg)](http://andvari.org)

Technical lead
==============
[![The British Museum logo](http://www.iath.virginia.edu/images/universal/IATH_logo.png)](http://www.iath.virginia.edu/)

UK partners
===========
[![The British Museum logo](https://finds.org.uk/assets/logos/bm_logo.png)](http://britishmuseum.org)
[![The Portable Antiquities Scheme logo](https://finds.org.uk/assets/logos/pas.jpg)](https://finds.org.uk)

Funded by:
==========
[![National Endowment for the Humanities logo](http://www.andvari.org/images/NEHlogo.jpg)](http://www.neh.gov/)


