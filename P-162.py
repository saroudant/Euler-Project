"""HEXADECIMAL NUMBERS - Problem 162"""

"""Instead of considering all the numbers that have 0, 1 or A, let's consider all
the numbers that don't. For a length of n, this number is 13^n.

Now summing from 1 to 16 will be enough, thus 13/12*(13^16-1).
Finally, this value should be removed from 16^16"""

from math import pow

base = 16
non_relevant = 13
number_digits = 16

total_numbers = pow(base,number_digits)

total_non_relevant_one_digit_non_zero = (base-1)*(pow(base-1,number_digits)/(base-2) - 1/(base-2))
total_non_relevant = (base-non_relevant)*total_non_relevant_one_digit_non_zero

total_numbers = int(total_numbers)
total_non_relevant = int(total_non_relevant)

hex_format = hex(total_numbers-total_non_relevant)
hex_format = str(hex_format)
hex_format = hex_format[3:]
hex_format = hex_format.upper()

print hex_format
#print result_hex

