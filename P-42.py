"""CODED TRIANGLE NUMBERS Problem-42

is_triangle : resolved the second-order equation n^2+n=2x and returns True in case
the result is an integer.

After being read and parsed, the words list is crossed and each word is tested. Finally
the numbers of triangle words is computed using the last check."""

from string import ascii_uppercase
from math import sqrt

def is_triangle(x):
    return int((-1+sqrt(1+8*x))/2) == (-1+sqrt(1+8*x))/2

with open("grid pb42.txt","r") as file:
    #Read and parse words list.
    words = file.read()
    words = words.replace('"','')
    words = words.split(",")

    #Each word is tried and added if it is triangle.
    nb_triangle_words = 0
    for w in words:
        if is_triangle(sum([ascii_uppercase.index(l)+1 for l in w])):
            nb_triangle_words += 1

    print nb_triangle_words


