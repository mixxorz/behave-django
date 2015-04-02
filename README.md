# behave-django
Behave BDD integration for Django

## Features
* Web Browser Automation ready
* Database transactions per scenario
* Use Django's testing client
* Use unittest + Django assert library

## Installation

Install using pip

	pip install behave-django
    
Add `behave_django` to your `INSTALLED_APPS`

    INSTALLED_APPS += ('behave_django',)

Create the features directory in your project's root directory.

	features/
    	steps/
        	your_steps.py
        environment.py
        your-feature.feature

Setup your `environment.py` file

    from behave_django import environment

    def before_scenario(context, scenario):
        environment.before_scenario(context, scenario)

    def after_scenario(context, scenario):
        environment.after_scenario(context, scenario)

Run `python manage.py behave`

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

## TODO
* You should be able to set where you features directory will be.
* You should be able to pass regular behave command line args.
* You should see behave's unimplemented step hints.
* Support for Django 1.4.x, 1.6.x, 1.7.x, 1.8 on Python 2.6, 2.7, 3, 3.3, 3.4.

## Contributing
[Read the quick contributing guide](CONTRIBUTING.md)


## Changelog
### 0.1.0
* Initial release
