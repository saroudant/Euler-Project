"""ORDERED FRACTIONS

If y is given, then
x/y - 3/7 is maximum for x = E(3/7*y)

For each denumerator value this value is taken and we consider the inverse
of the difference (to beeasily stored). Then the final list is sorted and
the first value is taken."""



d_max = 1000000
num_max = 3
den_max = 7
num_min = 2
den_min = 5

list_before = []
for den in range(1,d_max):
    if den == 7:
        continue

    num = int(3*den/7.)
    if den_max*num-num_max*den < 0:
        list_before.append((num,den,den_max*den/float(-den_max*num + num_max*den)))

list_before.sort(key=lambda x:x[2])

print list_before[-1][0]