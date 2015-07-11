from optparse import OptionParser, BadOptionError, AmbiguousOptionError


class PassThroughOptionParser(OptionParser):

    """
    An unknown option pass-through implementation of OptionParser.

    When unknown arguments are encountered, bundle with largs and try again,
    until rargs is depleted.

    sys.exit(status) will still be called if a known argument is passed
    incorrectly (e.g. missing arguments or bad argument types, etc.)

    Source: http://stackoverflow.com/a/9307174
    """

    def _process_args(self, largs, rargs, values):
        while rargs:
            try:
                OptionParser._process_args(self, largs, rargs, values)
            except (BadOptionError, AmbiguousOptionError) as e:
                largs.append(e.opt_str)
