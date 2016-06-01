"""Problem 100 - ARRANGED PROBABILITY

This problem is strictly equivalent to a diophantine equation.
If Xn is the number of blue discs and Yn the number of red ones, then :
Xn*(Xn - 1) = 1/2 * Yn *(Yn - 1). Which can be solved (using a solver) as
X(n+1) = 3Xn + 2Yn - 2
Y(n+1) = 4Xn + 3Yn - 3
Now we just have to find the first value of n for which Yn goes above 10^12
and take the corresponding Xn"""

threshold = 10**12

X = 15
Y = 21

while Y < threshold:
    X,Y = 3*X + 2*Y - 2, 4*X + 3*Y - 3

print X