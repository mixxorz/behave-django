from behave_django.testcase import BehaveDjangoTestCase

def before_scenario(context, scenario):
    context.test = BehaveDjangoTestCase()
    context.test.setUpClass()
    context.base_url = context.test.live_server_url
    
def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test