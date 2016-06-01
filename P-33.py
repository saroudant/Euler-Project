"""DIGIT CANCELLING FRACTIONS Problem-33

* try_other : try each combinaison for the common digit. In case a match is found, True
is returned.
* For each relevant fraction, try_other is tested.  In the end, the list of 2-digit fractions
is returned and can be processed.
* The three fractions are multiplied.
* The fraction is reduced and the denominator is printed."""

def try_other(num,den):
    same_dig = set([e for e in str(num)]).intersection(set([e for e in str(den)]))

    for e in same_dig:
        #num/den is changed by removing e and testing to be not trivial and equal to the former value
        new_num = int('0'+str(num).replace(e,'')) #0 is added to avoid type problem
        new_den = int('0'+str(den).replace(e,''))

        if new_num * den == new_den * num and new_num != 0 and new_den != 0 and num / 10. != new_num:
            return True

    return False

#Function for the reduce
def multiply(x,y):
    return x*y

#Next functions are here to give the PGCD of two values (taking the max)
def divisors(n):
    return [i for i in range(2,n+1) if n%i == 0]

def common_divisors(n1,n2):
    return list(set(divisors(n1)).intersection(set(divisors(n2))))


mn = 10
mx = 100

list_cancelled = [(i,j) for i in range(mn,mx) for j in range(i+1,mx) if try_other(i,j)]
denominator = [j for i,j in list_cancelled]
numerator = [i for i,j in list_cancelled]

denominator = reduce(multiply,denominator,1)
numerator = reduce(multiply,numerator,1)
same_factors = common_divisors(denominator,numerator)

print denominator / max(same_factors)