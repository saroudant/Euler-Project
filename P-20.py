"""FACTORIAL DIGIT SUM - Pb 20
100! would be too big for the computer to store.
Furthermore, 0 does not count into the final product, therefore we can remove
the 0 in the end of the value whenever there are some to keep only the
relevant part.
easy_factorial gives you the value not divisible by 10 of the factorial.
This value is then sumed up"""

def easy_factorial(k):
    if k in [0,1]:
        return 1
    else:
        value = k * easy_factorial(k-1)
        while value % 10 == 0:
            value /= 10
        return value

k = 100
print sum([int(e) for e in str(easy_factorial(k))])
