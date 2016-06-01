"""POWERFUL DIGIT SUM Problem-56

Brutal method."""

def sum_digits(n):
    """ Transforms an int into a string
    Sums the components.
    """
    str_n = str(n)

    return sum([int(x) for x in str_n])


a_max = 100
b_max = 100

m = 0
for a in xrange(a_max):
    for b in xrange(b_max):
        m = max(m,sum_digits(a**b))

print m