from behave_django import environment


def before_scenario(context, scenario):
    environment.before_scenario(context, scenario)


def after_scenario(context, scenario):
    environment.after_scenario(context, scenario)


def before_feature(context, feature):
    if feature.name == 'Fixture loading':
        context.fixtures = ['behave-fixtures.json']
