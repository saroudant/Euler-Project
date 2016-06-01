"""COUNTING SUMMATIONS Problem-76

number_perm : number of different summations for i+1. In the beginning, the
only known value is that 1 = 1. For the other no summation is known.

Then, for each element k between 2 and 100, the number of permutations is equal to
the sum of the number of permutations for k-i with only values below k-i (for i < k).
Therefore the only way is to add the values iteratively.

There cannot be any superposition since at the iteration i, number_perm[k] contains the
number of permutations using only values below i and only permutation using k-i are added."""

target = 100
number_perm = [1] + [0]*target

for i in range(1,target):
    for k in range(i,target+1):
        number_perm[k] += number_perm[k-i]

print number_perm[-1]