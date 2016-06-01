"""LEXICOGRAPHICS PERMUTATIONS Problem-24
The idea is to use combinatory.
For the first character, if its value is i, then lexicographically it will be
between i*9! + 1 and (i+1)*9!. We then have to find i such that the target fall in between.
This process is then reproduced iteratively by addin the current value."""

def factorial_list(n):
    l = [1]
    for i in xrange(n):
        l.append(l[-1]*(i+1))
    return l

mx = 9
n = mx
target = 1000000

factor = factorial_list(mx)
numbers = [e for e in xrange(mx+1)]
permutation = []
total = 1 #We start the ranking at 1

while n >= 0:
    index_add = (target - total) // factor[n]
    total += index_add * factor[n]
    permutation.append(numbers[index_add])
    numbers = numbers[:index_add] + numbers[index_add+1:]
    n -= 1

print "".join([str(e) for e in permutation])