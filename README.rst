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

Getting started
---------------

`Read the wiki! <https://github.com/mixxorz/behave-django/wiki/Getting-started>`__

Support
-------

behave-django is tested on Django 1.7.7 and 1.8 on Python 2.7, 3.3 and 3.4. However, it may work with other setups.

Contributing
------------

`Read the quick contributing guide <CONTRIBUTING.md>`__

Changelog
---------

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
