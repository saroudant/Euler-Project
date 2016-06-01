"""COMBINATORIC SELECTIONS Problem-53

In order to cack this problem, let's use the Pascal equality:
C(k,n) = C(k-1,n-1)+C(k,n-1).
Therefore, given the first line, every element until 100 can be computed
easily without the brutal factorial definition. Then the value above 10^6
are taken and counted."""

mx = 100
target = 1000000

#At the beginning, the only known value is C(0,0) = 1
#mx+1 is taken in order to go until 100 and not 99
combinations = [[0 for i in xrange(mx+1)] for j in xrange(mx+1)]
combinations[0][0] = 1

#C(j,i) = 0 if j > i, thus to fill it:
for i in range(1,mx+1):
    for j in xrange(i+1):
        combinations[i][j] = combinations[i-1][j-1] + combinations[i-1][j]

#Time to count
list_above_target = [sum([1 for x in e if x > target]) for e in combinations]
print sum(list_above_target)