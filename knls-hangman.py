from random import choice as choice
import json
#dictionary = open('dictionary.txt')
#word = json.load('dictionary')

dictionary = ["apple","ball","cat","dog","elephant"]
word = choice(dictionary)
print(word)

print("welcome to hangman\n")

dashes = "_" * len(word)
print(dashes)
letters = ''

while dashes != word:
    print("used letters: " + letters)

    guess = input("guess a letter: ")

    letters += guess
    
    if guess in word:
    	index=word.index(guess)
    	dashes[index] = guess
    	print(dashes)


