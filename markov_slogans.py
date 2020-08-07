# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:39:54 2020

Data source is a complilation of random corporate slogans.
uses a markov chain to generate a random company slogan

improvements: make a stop condition

@author: patno_000
"""
#load training data
quotes = open('quotes1.txt','r').read()


import numpy as np

#turn into list
lines = quotes.split("\n")
entries = []
for line in lines:
    entries.append(line.split(",\n"))


for line in entries:
    print(line)

x_text = lines

len(x_text)
#x_text[0][0:2]
#order is number of characters for current state
#markov chain bases off current state (order characters)
#then randojmly selects next state (next character)
order = 4

#makes random starting point
start = []
for i in range(len(x_text)):
    start.append(x_text[i][0:order])
#build transition "matrix"
#for each n-gram length "order", tally up possible characters after
grams = dict()
for line in x_text:
    for i in range(len(line)-order +1):
        gram = line[i:i+order]
        if not gram in grams:
            grams[gram] = []
        grams[gram].append(line[i+order:i+order+2])


beginings = []

#function to generate random slogans
def markovSlogan(no = 10):
    strt = np.random.choice(start)
    currentgram = strt
    reslt = currentgram
    for i in range(no):
        possbl = grams[currentgram]
        nxt = np.random.choice(possbl)
        reslt = reslt + nxt
        leng = len(reslt)
        currentgram = reslt[leng-order:leng]
    return reslt
    
markovSlogan(35)











