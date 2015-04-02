from behave_django.testcases import BehaveDjangoTestCase

def before_scenario(context):
    context.test = BehaveDjangoTestCase()
    context.test.setUpClass()
    context.base_url = context.test.live_server_url
    
def after_scenario(context):
    context.test.tearDownClass()
    del context.test