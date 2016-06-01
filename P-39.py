"""INTEGER RIGHT TRIANGLES Problem-39
* First the list of all possible cases is drawn using Pythagore theorem.
* Then for each perimeter the number of cases is computed.
* Finally the argmax is found using the dictionnary structure."""

from math import sqrt,floor

threshold = 1000

#All possible right triangles with integer sides.
list_tuples = [(i,j,sqrt(i**2+j**2)) for i in xrange(threshold) for j in xrange(threshold-i)]
list_tuples = [e for e in list_tuples if sum(e) <= threshold and floor(e[2]) == e[2] and e[0] > 0 and e[1] > 0]

#Dict for all values of perimeters
values = dict()
for v in xrange(threshold):
    values[v+1] = 0

for e in list_tuples:
    values[int(sum(e))] += 1

max_values = max([values[e] for e in values])
argmax_values = [e for e in values if values[e] == max_values]

print argmax_values
