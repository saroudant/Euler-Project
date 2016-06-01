"""COLLATZ CHAINE Problem 14
In order not to make too much recursive calls, previous values are stored into
a list intialized at 0.
Iteratively the maximum is computed and dropped in the end."""

def collatz(n,i,l,m):
    if n == 1:
        return i
    elif n < m and l[n] > 0:
        return l[n]+i-1
    elif n % 2 == 0:
        j = collatz(n/2,i+1,l,m)
        return j
    else:
        j = collatz(3*n+1,i+1,l,m)
        return j

m = 1000000
l = [0 for i in xrange(m)]
mx = 0
ind = 0
for i in range(1,m):
    l[i] = collatz(i,1,l,m)
    if mx < l[i]:
        mx = l[i]
        ind = i

print ind
