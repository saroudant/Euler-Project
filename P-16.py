"""POWER DIGIT SUM - Pb 16
Since 2^1000 is too big to be tested using usual integer representation
a list representation is chosen instead. First the multiplication is defined
and then applied iteratively"""

def multiply(l,a):
    n = len(l)
    for i in xrange(n):
        l[i] *= a

    for i in xrange(n):
        if i < n - 1:
            l[i+1] += l[i] // 10
            l[i] = l[i] % 10
        elif i == n - 1:
            if l[i] * a >= 10:
                l.append((l[i]) // 10)
            l[i] = (l[i]) % 10
    return l

a = 2
l = [2]
i = 1
mx = 1000

while i < mx:
    i += 1
    l = multiply(l,a)

print sum(l)


