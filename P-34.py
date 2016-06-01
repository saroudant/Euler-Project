"""DIGIT FACTORIAL Problem-34
* We take the biggest element such that n <= log(n) * 9!
* Every element in between is tested"""

from math import log

def factorial(n):
    list_factorial = [1]
    for i in range(1,n+1):
        list_factorial.append(list_factorial[i-1]*i)
    return list_factorial

fact_list = factorial(9)

mx = 2
while mx <= log(mx) * fact_list[-1]:
    mx += 2

list_fact_decomp = []
for i in range(10,mx):
    if sum([fact_list[int(e)] for e in str(i)]) == i:
        list_fact_decomp.append(i)

print sum(list_fact_decomp)