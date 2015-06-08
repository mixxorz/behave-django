Release History
---------------

0.1.4 (2015-06-08)
++++++++++++++++++

**Features and Improvements**

- `context.get_url()`. URL helper attached to context with built-in reverse resolution as a handy shortcut.

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
- Removed BEHAVE\_FEATURES setting in favor of using behave's configuration file

0.1.1 (2015-04-04)
++++++++++++++++++

**Features and Improvements**

- Behave management command now accepts behave command line arguments
- BEHAVE\_FEATURES settings added for multiple feature directories

**Bugfixes**

- Removed test apps and projects from the release package

0.1.0 (2015-04-02)
++++++++++++++++++

-  Initial release
