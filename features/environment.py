from behave_django import environment


def before_feature(context, feature):
    if feature.name == 'Fixture loading':
        context.fixtures = ['behave-fixtures.json']


def before_scenario(context, scenario):
    if scenario.name == 'Load fixtures for this scenario and feature':
        context.fixtures.append('behave-second-fixture.json')

    environment.before_scenario(context, scenario)


def after_scenario(context, scenario):
    environment.after_scenario(context, scenario)
