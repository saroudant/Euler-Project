"""CUBE DIGIT PAIRS Problem-90

is_satisfied : take a tuple that represents two dices and two arrangements and return True
is this tuple can indeed be realised.

Then each arrangements set is tested and added to the total if all squares can be indeed made."""

from itertools import combinations

def is_satisfied(arang,deck_a,deck_b):
    """
    Return true is the arang (a,b) can be satisfied by the two dices.
    :param arang: a tuple of two integers between 0 and 9
    :param deck_a: the first deck
    :param deck_b: the second one
    :return:
    """
    return (arang[0] in deck_a and arang[1] in deck_b) or (arang[1] in deck_a and arang[0] in deck_b)

list_values = [0,1,2,3,4,5,6,7,8,9]
list_square_tuples = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
nb_faces = 6

nb_arang = 0
deck_a = []
deck_b = []

for arang_a in combinations(list_values,nb_faces):
    for arang_b in combinations(list_values,nb_faces):
        #Decks are transformed into lists to add 9 or 6 if this is due.
        deck_a = list(arang_a)
        if 6 in deck_a:
            deck_a.append(9)
        if 9 in deck_a:
            deck_a.append(6)

        deck_b = list(arang_b)
        if 6 in deck_b:
            deck_b.append(9)
        if 9 in deck_b:
            deck_b.append(6)

        is_good = True
        for square in list_square_tuples:
            if not(is_satisfied(square,deck_a,deck_b)):
                is_good = False
                break

        nb_arang += is_good


#The number of found arangements has to be divided by two because arangements have be tried twice.
print nb_arang / 2