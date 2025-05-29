import random

def generate_word():

    words=[ ]

    with open("words_reqd_hangman.txt",'r') as f:

        for line in f:
            words.append(line.split()[0])

        for i in words:
            i=i.lower()

        return random.choice(words)
