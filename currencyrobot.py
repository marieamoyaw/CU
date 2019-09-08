"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Aion Ashby and Maxine Nzegwu and Nnenna Dara
Date:   7 September 2019
"""
import introcs


def before_space(s):

    """
    Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    x = s.index(" ")
    first = s[:x]
    return first


def after_space(s):

    """
    Returns: Substring of s after the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    y = s.index(" ")
    second = s[y+1:]
    return second


def first_inside_quotes(s):

    """
    Returns: The first substring of s between two (double) quote characters

    A quote character is one that is inside a string, not one that delimits
    it. We typically use single quotes (') to delimit a string if want to use
    a double quote character (") inside of it.

    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote
    characters inside.
    """
    x = s.index('"')
    first = s[x+1:]
    y = first.index('"')
    second = first[:y]
    return second


def get_src(json):

    """
    Returns: The SRC value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately
    following the keyword "src". For example, if the JSON is
        '{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros",
        "valid" : true, "error" : "" }'
    then this function returns '2 United States Dollars' (not '"2 United
    States Dollars"'). It returns the empty
    string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    a = json.find(':')
    b = json[a:]
    c = first_inside_quotes(b)
    return c


def get_dst(json):

    """
    Returns: The DST value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside double quotes (") \immediately following the keyword "dst".
    For example, if the JSON is

        '{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros",
        "valid" : true, "error" : "" }'
    then this function returns '1.727138 Euros' (not '"1.727138 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    a = json.find(',')
    b = json[a:]
    c = b.find(':')
    d = b[c:]
    e = first_inside_quotes(d)
    return e


def has_error(json):

    """
    Returns: True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the opposite of
    the value following the keyword "valid". For example, if the JSON is

        '{ "src" : "", "dst" : "", "valid" : false, "error" : "Source
        currency code is invalid." }'
    then the query is not valid, so this function returns True (It does NOT
    return the message 'Source currency code is invalid').
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    z = json.find("error")
    l = json[z:]
    y = l.find(":")
    m = l[y+1:]
    x = first_inside_quotes(m)
    w = "invalid" in x
    return w


def currency_response(currency_from, currency_to, amount_from):

    """
    Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form

        '{ "src" : "<old-amt>", "dst" : "<new-amt>", "valid" : true,
        "error" : "" }'
    where the values old-amount and new-amount contain the value and
    name for the original and new currencies.
    If the query is invalid, both old-amount and new-amount will be
    empty, while "valid" will be followed by the value false.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string with no spaces

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string with no spaces

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """

    s = 'http://cs1110.cs.cornell.edu/2018fa/a1server.php?from=' + \
    str(currency_from) + '&to=' + str(currency_to) + '&amt='+ str(amount_from)
    r = introcs.urlread(s)
    return r


def iscurrency(currency):

    """
    Returns: True if currency is a valid (3 letter code for a) currency. It
    returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string.

    In implementing iscurrency(), you should not use the table of currencies.
    That would make a very large function with a lot of if-statements.
    You are not allowed if-statements in this lab. Instead, you must use the
    functions currency_response and has_error as helper functions.
    """

    s = currency_response(currency, 'EUR', 2.5)
    y = has_error(s)
    return not y


def exchange(currency_from, currency_to, amount_from):

    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency
    currency_from to the currency currency_to. The value returned represents
    the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """

    s = currency_response(currency_from, currency_to, amount_from)
    x = get_dst(s)
    y = before_space(x)
    return float(y)
