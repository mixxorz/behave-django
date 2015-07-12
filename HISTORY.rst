Release History
---------------

0.2.2 (2015-07-13)
++++++++++++++++++

**Bugfixes**

- Fixed bug where positional arguments don't get sent to behave.

0.2.1 (2015-06-30)
++++++++++++++++++

**Bugfixes**

- Fixed bug where invalid arguments are passed onto behave, making the command fail to execute.

0.2.0 (2015-06-27)
++++++++++++++++++

**Features and Improvements**

- Integration with :code:`behave` is now done via monkey patching. Including the :code:`environment.before_scenario()` and :code:`environment.after_scenario()` function calls in your :code:`environment.py` file is no longer needed.
- A new CLI option, :code:`--use-existing-database`, has been added. See the `usage docs <https://pythonhosted.org/behave-django/usage.html#behave-command-line-options>`__.

**Bugfixes**

- Calling :code:`python manage.py behave --dry-run` does not create a test database any longer.

0.1.4 (2015-06-08)
++++++++++++++++++

**Features and Improvements**

- :code:`context.get_url()`. URL helper attached to context with built-in reverse resolution as a handy shortcut.

0.1.3 (2015-05-13)
++++++++++++++++++

**Features and Improvements**

- Fixture loading. You can now load your fixtures by setting :code:`context.fixtures`.
- behave-django now supports all versions of Django

**Bugfixes**

- The behave command should now correctly return non-zero exit codes when a test fails.

0.1.2 (2015-04-06)
++++++++++++++++++

**Features and Improvements**

- You can now have a :code:`.behaverc` in your project's root directory. You can specify where your feature directories are in this file, among other things. See the `behave docs on configuration files <https://pythonhosted.org/behave/behave.html#configuration-files>`__.
- Removed :code:`BEHAVE\_FEATURES` setting in favor of using behave's configuration file

0.1.1 (2015-04-04)
++++++++++++++++++

**Features and Improvements**

- Behave management command now accepts behave command line arguments
- :code:`BEHAVE\_FEATURES` settings added for multiple feature directories

**Bugfixes**

- Removed test apps and projects from the release package

0.1.0 (2015-04-02)
++++++++++++++++++

-  Initial release
