"""NUMBER SPIRAL DIAGONAL Problem 28
At each circle there are four integers to add.
The distance between two successive node in one circle grow of 2 from one circle to
the next.
The process is thus iteratively done so that the value are added."""

mx = 1001

tours = (mx // 2) + 1
inter_node = 2
total = 1
number = 1
for i in range(1,tours):
    for j in xrange(4):
        number += inter_node
        total += number
    inter_node += 2

print total