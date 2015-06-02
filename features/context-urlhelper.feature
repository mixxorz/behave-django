Feature: URL helpers are available in behave's context
    In order to ensure that url helpers are available as documented
    As the Maintainer
    I want to test all suggested uses

    Scenario: get_url() is an alias for the base_url property
        When I call get_url() without arguments
        Then it returns the value of base_url

    Scenario: The first positional argument in get_url() is attached as path to the base_url
        When I call get_url("/path/to/page/") with one positional argument
        Then the result is the base_url with "/path/to/page/" appended

    Scenario: Using the reverse keyword argument is identical to passing reverse(...) as first positional argument
        When I call get_url(reverse="admin:password_change") with the reverse keyword argument
        Then this returns the same result as get_url(reverse("admin:password_change"))

    Scenario: When two positional arguments are passed the second argument is ignored silently
        Given get_url(reverse="admin:password_change") returns a different value than get_url(path="/foo/bar/baz")
        When I call get_url("/foo/bar/baz", "admin:password_change") with two positional arguments
        Then this returns the same result as get_url("/foo/bar/baz")

    Scenario: When two keyword arguments are passed the result is constructed with the path keyword value
        Given get_url(reverse="admin:password_change") returns a different value than get_url(path="/foo/bar/baz")
        When I call get_url(reverse="admin:password_change", path="/foo/bar/baz") with two keyword arguments
        Then this returns the same result as get_url("/foo/bar/baz")
