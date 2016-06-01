"""Problem 74 - DIGIT FACTORIAL CHAINS

Computing the sum of digits' factorials : first the list of factorials between
0 and 9 are computed. Then the structure of Python's list is used to compute it
quickly.

Euler Project gives us the list of integers that are self looped (in the sens that
we go back to square one eventually). This list is stored in a dictionnary with the
corresponding length of the cycle.

Finally, for each number, the list will stop if and only if one of the previous integers
is reached. The loop is thus broken once one of those integers is reached."""

from itertools import permutations

def sum_digits_fact(n,list_factorials):
    """
    Return the sum of the digits factorials
    :param n: integer we want the integers to be computed
    :param list_factorials: List of the digits factorial
    :return:
    """
    n_list = [list_factorials[int(d)] for d in str(n)]
    return sum(n_list)

end = 10**6
start = 0
target = 60

#List of factorials between 0 and 9
list_factorials = [1]
for i in range(1,10):
    list_factorials.append(list_factorials[-1]*i)

#Stopping list that have been given
self_looped = dict()
self_looped[169] = 3
self_looped[363601] = 3
self_looped[1454] = 3
self_looped[871] = 2
self_looped[45361] = 2
self_looped[872] = 2
self_looped[45362] = 2
self_looped[1] = 1
self_looped[2] = 2
self_looped[145] = 1
self_looped[40585] = 1
self_looped['list'] = [1,2,145,169,363601,1454,871,45361,872,45362,40585]



nb_found = 0
i = start

while i < end:

    list_inter = [i]
    while list_inter[-1] not in self_looped['list']:
        list_inter.append(sum_digits_fact(list_inter[-1],list_factorials))

    if len(list_inter) + self_looped[list_inter[-1]] - 1 == target:
        nb_found += 1

    i += 1

print nb_found