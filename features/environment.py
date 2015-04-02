from behave_django import environment


def before_scenario(context, scenario):
    environment.before_scenario(context, scenario)
    
def after_scenario(context, scenario):
    environment.after_scenario(context, scenario)