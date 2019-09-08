"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
amount.
It prints out the result of converting the first currency to the second.

Author: Aion Ashby and Maxine Nzegwu and Nnenna Dara
Date:   7 September 2019
"""

import a1

original = input('3-letter code for original currency: ')
new = input('3-letter code for the new currency: ')
amount = input('Amount of the original currency: ')
print('You can exchange ' + amount + ' ' + original + ' for ' +\
 str(a1.exchange(original, new, float(amount))) + ' ' + new + '.')
