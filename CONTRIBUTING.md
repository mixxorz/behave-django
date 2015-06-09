# Contributing

Wanna help out with behave-django? Cool! Here's a quick guide to do just that.

Fork, then clone the repo:

```bash
    $ git clone git@github.com:your-username/behave-django.git
```

Install the dependencies

```bash
    $ pip install -r requirements.txt
```

Make sure the tests pass. The `@failing` tag is used for tests that are supposed to fail.

```bash
    $ python manage.py behave --tags=~@failing  # skip failing tests
    $ python tests.py
```

Start your topic branch

```bash
    $ git checkout -b your-topic-branch
```

Make your change. Add tests for your change. Make the tests pass:

```bash
    $ python manage.py behave --tags=~@failing
    $ python tests.py
```

Your tests don't have to be behave tests. :smile:

Push to your fork and [submit a pull request][pr].

[pr]: https://github.com/mixxorz/behave-django/compare/

Other things to note:

- Write tests.
- We're using PEP8 as our code style guide

Thank you! :grinning:
