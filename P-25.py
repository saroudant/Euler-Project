"""1000-digit Fibonacci number Problem-25
Fn is the sum of two terms ; one of which decreases to 0 exponentially.
This term is neglected, the log has been taken and solved."""

from math import log,sqrt,floor

target = 1000
phi = (1 + sqrt(5)) / 2
print floor((target - 1 + 1. / 2. * log(5,10)) / log(phi,10)) + 1
