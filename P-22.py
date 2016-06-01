"""NAMES SCORES Problem-22
* First the names are parsed in order to have them in the form of a list.
* alphabet gives the list of the letters ranked alphabetically.
* name_scores give the products.
* names_scores is then sumed to have the product."""

with open("grid pb22.txt","r") as file:
    #First the list is parsed
    names = file.read()
    names = names.split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]

    #Then the list is sorted
    names.sort()

    #List of letters
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    alphabet = alphabet.split(" ")
    alphabet_rank = dict()
    for i,letter in enumerate(alphabet):
        alphabet_rank[letter] = i

    names_scores = [(rank+1) * sum([alphabet_rank[letter]+1 for letter in word]) for rank,word in enumerate(names)]

    print sum(names_scores)