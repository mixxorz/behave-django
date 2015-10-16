# Contributing

Wanna help out with behave-django? Cool! Here's a quick guide to do just that.

Fork, then clone the repo:

```bash
    $ git clone git@github.com:your-username/behave-django.git
```

Install the dev dependencies

```bash
    $ pip install -r requirements-dev.txt
```

Make sure the tests pass. The `@failing` tag is used for tests that are supposed to fail.

```bash
    $ python manage.py behave --tags=~@failing  # skip failing tests
    $ py.test
```

Start your topic branch

```bash
    $ git checkout -b your-topic-branch
```

Make your changes. Add tests for your change. Make the tests pass:

```bash
    $ python manage.py behave --tags=~@failing
    $ py.test
```

Finally, make sure your tests pass on all the configurations behave-django supports. We use tox for this. Python 2.6, 2.7, 3.3 and 3.4 needs to be available in your PATH.

```bash
    $ tox
```

You can choose not to run the tox tests, but make sure your tests pass in the CI server when you push your PR.

Your tests don't have to be behave tests. :smile:

Push to your fork and [submit a pull request][pr].

[pr]: https://github.com/mixxorz/behave-django/compare/

Other things to note:

- Write tests.
- We're using PEP8 as our code style guide

Thank you! :grinning:
