"""
Unit test for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Aion Ashby and Maxine Nzegwu NetIDs: aea99 and man227
Date:   14 September 2018
"""

import introcs
import a1


def testA():
    """
    Test procedure for Part A
    """
    print("Testing function before_space(s)")
    s = "Hello World"
    answer = a1.before_space(s)
    introcs.assert_equals('Hello', answer)
    r = 'Hello my name is'
    result = a1.before_space(r)
    introcs.assert_equals('Hello', result)
    t = '     hi'
    final = a1.before_space(t)
    introcs.assert_equals('', final)
    q = 'bye    '
    last = a1.before_space(q)
    introcs.assert_equals('bye', last)
    print("The module is working correctly")

    print("Testing function after_space(s)")
    s = "Hello World"
    result = a1.after_space(s)
    introcs.assert_equals('World', result)
    w = 'Hello my name is'
    result = a1.after_space(w)
    introcs.assert_equals('my name is', result)
    t = '     hi'
    final = a1.after_space(t)
    introcs.assert_equals('    hi', final)
    q = 'bye    '
    last = a1.after_space(q)
    introcs.assert_equals('   ', last)
    m = 'hi  '
    final = a1.after_space(m)
    introcs.assert_equals(' ', final)
    x = 'hello '
    end = a1.after_space(x)
    introcs.assert_equals('', end)
    print("The module is working correctly")


def testB():
    """
    Test procedure for Part B
    """
    print("Testing function first_inside_quotes(s)")
    s = 'A "B C" D'
    answer = a1.first_inside_quotes(s)
    introcs.assert_equals('B C', answer)
    e = 'hello" " hi'
    result = a1.first_inside_quotes(e)
    introcs.assert_equals(" ", result)
    c = '"1"'
    result = a1.first_inside_quotes(c)
    introcs.assert_equals("1", result)
    t = '"hello" my "name is"'
    final = a1.first_inside_quotes(t)
    introcs.assert_equals("hello", final)
    e = '"" hi'
    result = a1.first_inside_quotes(e)
    introcs.assert_equals("", result)
    print('The module is working correctly')

    print("Testing function get_src(json)")
    s = '{ "src" : "     2 United States Dollars     ",\
     "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    final = a1.get_src(s)
    introcs.assert_equals('     2 United States Dollars     ', final)
    s = '{ "src" : "2 United States Dollars     ",\
     "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    final = a1.get_src(s)
    introcs.assert_equals('2 United States Dollars     ', final)
    s = '{ "src" : "     2 United States Dollars",\
     "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    final = a1.get_src(s)
    introcs.assert_equals('     2 United States Dollars', final)
    s = '{ "src" : "2 United States Dollars",\
     "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    final = a1.get_src(s)
    introcs.assert_equals('2 United States Dollars', final)
    s = '{ "src" : "",\
     "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'
    final = a1.get_src(s)
    introcs.assert_equals("", final)
    q = '{ "src" : "", "dst" : "", "valid" : false, "error" :\
     "Exchange currency code is invalid." }'
    end = a1.get_src(q)
    introcs.assert_equals("", end)
    print('The module is working correctly')

    print("Testing function dst_src(json)")
    s = '{ "src" : "2 United States Dollars", "dst" :\
     "     1.727138 Euros      ", "valid" : true, "error" : "" }'
    end = a1.get_dst(s)
    introcs.assert_equals('     1.727138 Euros      ', end)
    s = '{ "src" : "2 United States Dollars", "dst" :\
     "1.727138 Euros      ", "valid" : true, "error" : "" }'
    end = a1.get_dst(s)
    introcs.assert_equals('1.727138 Euros      ', end)
    s = '{ "src" : "2 United States Dollars", "dst" :\
     "     1.727138 Euros", "valid" : true, "error" : "" }'
    end = a1.get_dst(s)
    introcs.assert_equals('     1.727138 Euros', end)
    s = '{ "src" : "2 United States Dollars", "dst" :\
     "1.727138 Euros", "valid" : true, "error" : "" }'
    end = a1.get_dst(s)
    introcs.assert_equals('1.727138 Euros', end)
    s = '{ "src" : "2 United States Dollars",\
     "dst" : "", "valid" : true, "error" : "" }'
    final = a1.get_dst(s)
    introcs.assert_equals("", final)
    s = '{ "src" : "", "dst" : "", "valid" : false, "error"\
     : "Source currency code is invalid." }'
    stop = a1.get_dst(s)
    introcs.assert_equals("", stop)
    print('The module is working correctly')

    print('Testing has_error(json)')
    t = '{ "src" : "<old-amt>", "dst" : "<new-amt>", "valid" : true,\
    "error" : "" }'
    final = a1.has_error(t)
    introcs.assert_equals(False, final)
    q = '{ "src" : "", "dst" : "", "valid" : false, "error" :\
     "Exchange currency code is invalid." }'
    end = a1.has_error(q)
    introcs.assert_equals(True, end)
    l = '{ "src" : "", "dst" : "", "valid" : false, "error" :\
     "Currency amount is invalid." }'
    done = a1.has_error(l)
    introcs.assert_equals(True, done)
    s = '{ "src" : "", "dst" : "", "valid" : false, "error"\
     : "Source currency code is invalid." }'
    stop = a1.has_error(s)
    introcs.assert_equals(True, stop)
    print('The module is working correctly')


def testC():
    """
    Test procedure for Part C
    """

    print('Testing function currency_response(currency_from,\
     currency_to, amount_from)')
    last = a1.currency_response('USD', 'EUR', 2.5)
    introcs.assert_equals('{ "src" : "2.5 United States Dollars", "dst"'+\
    ' : "2.1589225 Euros", "valid" : true, "error" : "" }', last)
    last = a1.currency_response('United', 'EUR', 2.5)
    introcs.assert_equals('{ "src" : "", "dst" : "", "valid" : '+\
    'false, "error" : "Source currency code is invalid." }', last)
    last = a1.currency_response('USD', 'Europe', 2.5)
    introcs.assert_equals('{ "src" : "", "dst" : "", "valid" : '+\
    'false, "error" : "Exchange currency code is invalid." }', last)
    last = a1.currency_response('USD', 'EUR', 2.8989890)
    introcs.assert_equals('{ "src" : "2.898989 United States Dollars", "dst"'+\
    ' : "2.503477031741 Euros", "valid" : true, "error" : "" }', last)
    print('The module is working correctly')


def testD():
    """
    Test procedure for Part D
    """

    print('Testing function iscurrency(currency)')
    result = a1.iscurrency('United')
    introcs.assert_equals(False, result)
    result = a1.iscurrency('USD')
    introcs.assert_equals(True, result)
    result = a1.iscurrency('')
    introcs.assert_equals(False, result)
    print('The module is working correctly')

    print('Testing function exchange(currency_from, currency_to, amount_from)')
    result = a1.exchange('USD', 'EUR', 2.0)
    introcs.assert_floats_equal(1.727138, result)
    print('The module is working correctly')


testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
