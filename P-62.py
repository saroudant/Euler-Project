"""CUBIC PERMUTATIONS Problem-62

Rebase : order an integer's digits from the lowest to the biggest.

Each combinaison is tried iteratively and added to the permutations list (a permutation
is represented by its lowest permutation, ie. its ordered one). One a permutation has reached
the targeted number, then the loop is broken and the argument is printed."""

def rebase(n):
    """ Take an integer and return a string with ordered digits.
    EX : 87423 gives '23478'
    """
    str_n = str(n)

    list_n = [int(i) for i in str_n]
    list_n.sort()
    list_n = [str(i) for i in list_n]

    return "".join(list_n)


target = 5
power = 3

permutations = dict()

m = 0
n = 0
arg_min = 0
while m < target:
    r_n = rebase(n**power)
    if r_n in permutations:
        permutations[r_n][1] += 1
        if m < permutations[r_n][1]:
            m = permutations[r_n][1]
            arg_min = r_n
    else:
        permutations[r_n] = [n,1]
    n += 1

print permutations[arg_min][0] ** power