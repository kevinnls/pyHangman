import json
from random import choice as choice
from clear import clear as clear
def listify(string):
    n = 0
    l = []
    for i in string:
        l.append(i)
        n+=1
    return l
def dashify(dashes):
    for i in dashes:
        print(i ,end = " ")
    print ("\n")
def hangman():
    clear()
    print("welcome to hangman\n")
    dashify(dashes)

with open('dictionary.json') as dict:
    word = listify(choice(json.load(dict)))
    dashes = listify("_" * len(word))
    letters = []
    chances = 6
dict.close()    

hangman()
print("\n")

while dashes != word and chances>0:
    
    print("used letters: " + str(letters))
    print("chances left " + str(chances) +"/6")
    guess = input("guess a letter: ")
    
    ###tracking used letters###
    if len(guess)>1 or guess == '' :
        hangman()
        print("type one letter at a time please\n")
        continue
    elif guess in letters:
        hangman()
        print("this letter has already been used\n")
        continue
    elif guess not in letters:
        letters.append(guess)   
    ###tracking used letters###
    
    ###check letter in word###
    if guess in word:
        n=-1
        for i in word:
            n+=1
            if guess == i:
                dashes[n] = word[n]
        hangman()
        print("\n")
         
    elif guess not in word:
        chances-=1
        hangman()
        print("that letter is not in the word\n")
    
if chances>0:
    hangman()
    print("\ncongrats! you have won!")
else:
    hangman()
    print("\nsorry. you have lost.")
