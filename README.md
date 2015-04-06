# behave-django
[![Build Status](https://travis-ci.org/mixxorz/behave-django.svg?branch=master)](https://travis-ci.org/mixxorz/behave-django) [![Latest Version](https://pypip.in/version/behave-django/badge.svg)](https://pypi.python.org/pypi/behave-django/)

Behave BDD integration for Django

## Features
* Web Browser Automation ready
* Database transactions per scenario
* Use Django's testing client
* Use unittest + Django assert library
* Use behave's command line arguments
* Use behave's configuration file

## Getting started
[Read the wiki!](https://github.com/mixxorz/behave-django/wiki/Getting-started)

## Support
behave-django is tested on Django 1.7.7 and 1.8 on Python 2.7, 3.3 and 3.4. However, it may work with other setups.

## Contributing
[Read the quick contributing guide](CONTRIBUTING.md)

## Changelog
#### Unreleased
* FEATURE: Removed BEHAVE_FEATURES setting in favor of using [behave's configuration file](https://pythonhosted.org/behave/behave.html#configuration-files)

#### 0.1.1
* FEATURE: Behave management command now accepts behave command line arguments
* FEATURE: BEHAVE_FEATURES settings added for multiple feature directories
* BUGFIX: Removed test apps and projects from the release package

#### 0.1.0
* Initial release
