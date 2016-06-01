"""PENTAGON NUMBERS Problem-44
Every couple (j,k) for j > k is tested until the minimum value is found.
Each iteration the pentagon numbers list is changed to have the new values."""

pentagon_numbers = [1,5]
n = 3.

not_found = True
j = 0
k = 0
while not_found:
    if j <= k+1:
        j += 1
        k = 0
    else:
        k += 1
    #First the list is filled to have the proper values.
    while pentagon_numbers[j] + pentagon_numbers[k] > pentagon_numbers[-1]:
        pentagon_numbers.append(n*(3*n-1.)/2.)
        n += 1
    #Then we try to see if the couple j,k satisfies the condition. If so the loop will be stopped.
    not_found = not((pentagon_numbers[j] + pentagon_numbers[k] in pentagon_numbers) and (pentagon_numbers[j] - pentagon_numbers[k] in pentagon_numbers))

max_D = pentagon_numbers[j] - pentagon_numbers[k]
print max_D
