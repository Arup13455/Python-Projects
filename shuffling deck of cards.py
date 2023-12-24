# program to shuffle deck of cards
import random, itertools
deck = list(itertools.product(range(1,14),["spade","club","Hearts","Diamond"]))
random.shuffle(deck)
num = int(input("Enter a num of times you want to shuffle: "))
for i in range(num):
        print(deck[i][0],"of",deck[i][1])