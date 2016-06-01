"""Problem 38 - PANDIGITAL MULTIPLES

The maximum number is 100000 since this number will be concatenated twice
to be tested (the real maximum is much less but this figure is enough).
Then each number will be tested and the maximum taken."""

def is_pandigital(n):
    """ Sort the numbers of n and compares the list with [0,1,..,9]
    :param n: Integer you want to test
    :return: True if n is pandigital, False otherwise
    """
    list_n = str(n)
    list_n = [int(e) for e in list_n]
    list_n.sort()
    return list_n == range(1,10)

mx = 100000 #Could not be more than the max pandigital and need two concatenation

not_found = True
list_pandigitals_product = []

while mx > 0:
    k = str(mx)
    i = 2
    while len(k) < 9:
        k += str(mx*i)
        i += 1

    if is_pandigital(int(k)):
        list_pandigitals_product.append(int(k))
    mx -= 1

list_pandigitals_product.sort()
print list_pandigitals_product[-1]