# Contributing

Wanna help out with behave-django? Yay! Here's a quick guide to do just that.

Fork, then clone the repo:

    git clone git@github.com:your-username/behave-django.git

Install the dependencies

    pip install -r requirements.txt

Make sure the tests pass:

    python manage.py behave
    
Start your topic branch

	git checkout -b your-topic-branch

Make your change. Add tests for your change. Make the tests pass:

    python manage.py test

Your tests don't have to be behave tests. :smile:

Push to your fork and [submit a pull request][pr].

[pr]: https://github.com/mixxorz/behave-django/compare/

Other things to note:

* Write tests.
* We're using PEP8 as our code style guide

Thanks :)