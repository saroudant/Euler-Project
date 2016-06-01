"""NON-ABUNDANT SUM Problem 23
divisors : give the list of all divisors < n for n
d : give the sum of those divisors

* First the list of all abundants number below 28123 is drawn.
* Then the list of sums below 28123 is drawn.
* Finally the wanted value is computed using the difference to the sum of i."""

def divisors(n):
    return [i for i in range(1, n//2 + 1) if n%i == 0]

def d(n):
    return sum(divisors(n))

max_abundant = 28123

#List of abundants under 28123
list_abundants = [i for i in xrange(max_abundant) if d(i) > i]

#List of two-sum of abundant numbers. i < j in order to remove elements that could be there twice.
sum_abundants = [i+j for i in list_abundants for j in list_abundants if i+j <= max_abundant and i <= j]
dict_abundants = dict()
sum_sum_abundants = 0
for e in sum_abundants:
    if e not in dict_abundants:
        dict_abundants[e] = 0
        sum_sum_abundants += e

#List of int that are nbelow the max
all_integers = [i for i in range(1,max_abundant+1)]

#the difference is made to compute the sum of non abundant.
print sum(all_integers) - sum_sum_abundants