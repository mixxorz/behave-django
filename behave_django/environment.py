from behave_django.testcase import BehaveDjangoTestCase

def before_scenario(context, scenario):
    # This is probably a hacky method of setting up the test case
    # outside of a test runner. Suggestions are welcome. :)
    context.test = BehaveDjangoTestCase()
    context.test.setUpClass()
    context.test()
    context.base_url = context.test.live_server_url
    
def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test