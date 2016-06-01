"""POKER HANDS Problem-54

Poker_hand class :
    * Transform a string into three components : its values, its suits and a list of the
    cards.
    * Give the value of the hand, the biggest value of the "interesting" part and the other
    carts sorted.

comparison : compares 2 hands and return 1 if the first one won, 0 if not.

won : given two players given as one string, return the parsed comparison.

Then the given file is parsed and each set is tried.

I acknowledge this problem could have been solved in an easier way. I chose this solution because
it was the occasion for me to practice Oriented Object Programming."""

class Poker_hand:

    def __init__(self,hand_str):
        """
        A poker hand is represented by :
            * values : dictionnary of values. For each value between 2 and 14(A), values
            contains the number of this value.
            *suits : dictionnary of suits. For each suit, suits contains the list of values
            that have this suit.
            *hands : list of cards.
        :param hand_str: hand as it is given by Euler Project
        :return: a class instance
        """

        self.values = dict()
        for i in range(2,15):
            self.values[i] = 0

        self.suits = dict()
        for s in ['S','D','C','H']:
            self.suits[s] = []

        self.hands = hand_str.split(" ")

        for card in self.hands:
            card = card.replace("A",'14')
            card = card.replace("K",'13')
            card = card.replace("Q",'12')
            card = card.replace("J",'11')
            card = card.replace("T",'10')

            self.suits[card[-1]].append(int(card[:-1]))
            self.values[int(card[:-1])] += 1



    def hand_value(self):
        """
        Return the value of the hand. 0 if there is nothing, 1 if there is one pair,...,10 if there
        is a flush.
        Along side this, it returns the highest card of the making and the remaining best card (if there is one).
        :return:
        """

        #For a flush, all the cards have to have the same suit.
        if max([len(self.suits[x]) for x in self.suits]) == 5:

            #If they have the same suit, then two cards cannot have the same value.
            if min([x for x in self.values if self.values[x] != 0]) + 5 \
                    == max([x for x in self.values if self.values[x] != 0]):

                if self.values[14] == 1:
                    return 10,[14],[14]
                else:
                    i_max = [i for i in range(2,14) if self.values[i] != 0]
                    return 9,[max(i_max)],[max(i_max)]

        #Four of a kind and full house
        if max([self.values[x] for x in self.values]) == 4:

            return 8,[i for i in range(2,15) if self.values[i] == 4],[i for i in range(2,15) if self.values[i] == 1]

        elif max([self.values[x] for x in self.values]) == 3 \
                and min([self.values[x] for x in self.values if self.values[x] > 0]) == 2:

            return 7,[i for i in range(2,15) if self.values[i] == 3],sorted([i for i in range(2,15) if self.values[i] == 2])

        #Flush : one suit has 5 cards
        if max([len(self.suits[x]) for x in self.suits]) == 5:
            list_cards = [i for i in range(2,15) if self.values[i] != 0]
            list_cards.sort()
            return 6,[list_cards[-1]],list_cards[:-1]

        #To know if values are consecutive, the first value is removed.
        #The remaining list should be [0,1,2,3,4]
        list_cards = [i for i in range(2,15) if self.values[i] != 0]
        list_cards.sort()
        min_value = list_cards[0]
        list_cards = [e - min_value for e in list_cards]
        if list_cards == range(0,5):
            list_cards = [i for i in range(2,15) if self.values[i] != 0]
            list_cards.sort()
            return 5,list_cards[-1],list_cards[:-1]


        #Three of a kind
        if max([self.values[x] for x in self.values]) == 3:
            return 4,[i for i in self.values if self.values[i] == 3],\
                   [i for i in range(2,15) if self.values[i] in [1,2]]

        #When there are two doubles, three values are given : the two pairs and the other one.
        elif len([self.values[x] for x in self.values if self.values[x] == 2]) == 2:
            list_doubles = [x for x in self.values if self.values[x] == 2]
            list_doubles.sort()
            other = [x for x in self.values if self.values[x] == 1]
            other.sort()
            return 2,[list_doubles[-1]],other+list_doubles

        #When there is only one double, the double value is given and the list of the ordered remaining one.
        elif len([self.values[x] for x in self.values if self.values[x] == 2]) == 1:
            list_doubles = [x for x in self.values if self.values[x] == 2]
            list_doubles.sort()
            other = [x for x in self.values if self.values[x] == 1]
            other.sort()
            return 1,[list_doubles[-1]],other

        else:
            other = [x for x in self.values if self.values[x] == 1]
            other.sort()
            return 0,[other[-1]],other[:-1]



def comparison(A,B):
    """
    Takes two strings (sets), transforms them into poker hands and compare
    their value
    :param A: first hand
    :param B: second hand
    :return: 0 if B won, 1 otherwise
    """
    hand_A = Poker_hand(A)
    hand_B = Poker_hand(B)

    value_A = hand_A.hand_value()
    value_B = hand_B.hand_value()

    if value_A[0] > value_B[0]:
        return 1
    elif value_A[0] < value_B[0]:
        return 0
    elif value_A[1][-1] > value_B[1][-1]:
        return 1
    elif value_A[1][-1] < value_B[1][-1]:
        return 0
    elif value_A[2][-1] < value_B[2][-1]:
        return 0
    elif value_A[2][-1] > value_B[2][-1]:
        return 1
    elif value_A[2][-2] < value_B[2][-2]:
        return 0
    elif value_A[2][-2] > value_B[2][-2]:
        return 1
    elif value_A[2][-3] < value_B[2][-3]:
        return 0
    elif value_A[2][-3] > value_B[2][-3]:
        return 1
    elif value_A[2][-4] < value_B[2][-4]:
        return 0
    elif value_A[2][-4] > value_B[2][-4]:
        return 1
    elif value_A[2][-5] < value_B[2][-5]:
        return 0
    elif value_A[2][-5] > value_B[2][-5]:
        return 1



def won(st):
    """
    Compare a given line
    :param st: A line of the given file
    :return: 1 if the first player won, 0 otherwise
    """
    return comparison(st[:14],st[-14:])



with open('grid pb54.txt',"r") as file:
    games = file.read()
    games = games.split('\n')

    total = [won(e) for e in games if len(e) > 0]
    print sum(total)