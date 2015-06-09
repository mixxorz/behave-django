************
Installation
************

Install using pip

.. code-block:: python

    $ pip install behave-django

Add :code:`behave_django` to your :code:`INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = ('
        ...
        behave_django',
        ...
    )

Create the features directory in your project's root directory. (Next to `manage.py`)

.. code-block::

    features/
        steps/
            your_steps.py
        environment.py
        your-feature.feature

Setup your `environment.py` file

.. code-block:: python

    from behave_django import environment

    def before_scenario(context, scenario):
        environment.before_scenario(context, scenario)

    def after_scenario(context, scenario):
        environment.after_scenario(context, scenario)

Run :code:`python manage.py behave`

.. code-block::

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

