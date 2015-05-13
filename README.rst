behave-django
=============

|Build Status| |Latest Version|

Behave BDD integration for Django

Features
--------

-  Web Browser Automation ready
-  Database transactions per scenario
-  Use Django's testing client
-  Use unittest + Django assert library
-  Use behave's command line arguments
-  Use behave's configuration file
-  Fixture loading

Getting started
---------------

`Read the wiki! <https://github.com/mixxorz/behave-django/wiki/Getting-started>`__

Support
-------

behave-django is tested on:

Django 1.4.20, 1.5.12, 1.6.11, 1.7.7, 1.8

Python 2.6, 2.7, 3.3, 3.4

It should work on everything, basically.

Contributing
------------

`Read the quick contributing guide <CONTRIBUTING.md>`__

Changelog
---------

0.1.3
^^^^^

-  FEATURE: Fixture loading. You can now load your fixtures by setting :code:`context.fixtures`.
-  BUGFIX: behave-django now supports all versions of Django
-  BUGFIX: The behave command should not correctly return non-zero exit codes when a test fails.

0.1.2
^^^^^

-  FEATURE: You can now have a :code:`.behaverc` in your project's root directory. You can specify where your feature directories are in this file, among other things. See the `behave docs on configuration files <https://pythonhosted.org/behave/behave.html#configuration-files>`__.
-  FEATURE: Removed BEHAVE\_FEATURES setting in favor of using behave's configuration file

0.1.1
^^^^^

-  FEATURE: Behave management command now accepts behave command line arguments
-  FEATURE: BEHAVE\_FEATURES settings added for multiple feature directories
-  BUGFIX: Removed test apps and projects from the release package

0.1.0
^^^^^

-  Initial release

.. |Build Status| image:: https://travis-ci.org/mixxorz/behave-django.svg?branch=master
   :target: https://travis-ci.org/mixxorz/behave-django
.. |Latest Version| image:: https://pypip.in/version/behave-django/badge.svg
   :target: https://pypi.python.org/pypi/behave-django/
