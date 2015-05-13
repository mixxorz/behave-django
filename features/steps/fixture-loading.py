from behave import then

from test_app.models import BehaveTestModel


@then(u'the fixture should be loaded')
def check_fixtures(context):
    context.test.assertEqual(BehaveTestModel.objects.count(), 1)
