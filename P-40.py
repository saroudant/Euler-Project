"""CHAMPERNOWNE'S CONSTANT Problem-40
Since the integer implementation is not big enough to support 10^6 numbers
for an integer, it has been decided to use the string structure.
This string is being concatenated to the list of the integers in the order.
Then the product is done using the big computed string."""

from math import log

threshold = 1000000

#The string is concatenated.
concat_int = ''
i = 1
while len(concat_int) <= threshold:
    concat_int += str(i)
    i += 1

#The product is made using previous string.
product = 1
for i in xrange(0,int(log(threshold,10))+2):
    product *= int(concat_int[10**i-1])

print product