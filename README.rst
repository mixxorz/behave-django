behave-django
=============
.. intro-marker

|Build Status| |Latest Version| |Downloads|

Behave BDD integration for Django

.. features-marker

Features
--------

-  Web Browser Automation ready
-  Database transactions per scenario
-  Use Django's testing client
-  Use unittest + Django assert library
-  Use behave's command line arguments
-  Use behave's configuration file
-  Fixture loading

.. support-marker

Support
-------

behave-django supports all current Django and Python versions.
Specifically, our tests cover:

Django 1.4.20, 1.5.12, 1.6.11, 1.7.8, 1.8.2, and Python 2.6, 2.7, 3.3, 3.4.

.. install-marker

Installation
------------

Install using pip

::

    $ pip install behave-django

Add ``behave_django`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS += ('behave_django',)

Create the features directory in your project’s root directory. (Next to
``manage.py``)

::

    features/
        steps/
            your_steps.py
        environment.py
        your-feature.feature

Setup your ``environment.py`` file

::

    from behave_django import environment

    def before_scenario(context, scenario):
        environment.before_scenario(context, scenario)

    def after_scenario(context, scenario):
        environment.after_scenario(context, scenario)

Run ``python manage.py behave``

::

    $ python manage.py behave
    Creating test database for alias 'default'...
    Feature: Running tests # features/running-tests.feature:1
      In order to prove that behave-django works
      As the Maintainer
      I want to test running behave against this features directory
      Scenario: The Test                       # features/running-tests.feature:6
        Given this step exists                 # features/steps/running_tests.py:4 0.000s
        When I run "python manage.py behave"   # features/steps/running_tests.py:9 0.000s
        Then I should see the behave tests run # features/steps/running_tests.py:14 0.000s

    1 features passed, 0 failed, 0 skipped
    1 scenarios passed, 0 failed, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 0 undefined
    Took.010s
    Destroying test database for alias 'default'...

.. note::

   Starting with version ``0.2.0``, you no longer need to insert the ``environment.before_scenario()`` and ``environment.after_scenario()`` functions in your ``environment.py`` file. The hooks are now included via monkey patching.

.. docs-marker

Documentation
-------------

-  Documentation is available from `pythonhosted.org/behave-django`_
-  Read more about *behave* at `pythonhosted.org/behave`_

.. contribute-marker

How to Contribute
-----------------

Please, read the `contributing guide`_.


.. _pythonhosted.org/behave-django: https://pythonhosted.org/behave-django/
.. _pythonhosted.org/behave: http://pythonhosted.org/behave/
.. _contributing guide: https://github.com/mixxorz/behave-django/blob/master/CONTRIBUTING.md
.. |Build Status| image:: https://img.shields.io/travis/mixxorz/behave-django/master.svg
    :target: https://travis-ci.org/mixxorz/behave-django
.. |Latest Version| image:: https://img.shields.io/pypi/v/behave-django.svg
    :target: https://pypi.python.org/pypi/behave-django/
.. |Downloads| image:: https://img.shields.io/pypi/dm/behave-django.svg
    :target: https://pypi.python.org/pypi/behave-django/
