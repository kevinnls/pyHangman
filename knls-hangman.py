import clear
import json
from random import choice as choice
#from clear import clear as clear
from listify import listify as listify
from dashify import dashify as dashify
with open('dictionary.json') as dict:
    word = listify(choice(json.load(dict)))
    dashes = listify("_" * len(word))
    letters = []
    chances = 6
    
print("welcome to hangman\n")
dashify(dashes)

while dashes != word and chances>0:
    
    print("used letters: " + str(letters))
    print("chances left " + str(chances) +"/6")
    guess = input("guess a letter: ")
    
    ###tracking used letters###
    if len(guess)>1:
        clear.clear()    
        print("welcome to hangman\n")
        dashify(dashes)
        print("type only one letter at a time please")
        continue
    elif guess in letters:
        clear.clear()
        print("welcome to hangman\n")
        dashify(dashes)
        print("this letter has already been used")
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
        clear.clear()    
        print("welcome to hangman\n")
        dashify(dashes)       
         
    elif guess not in word:
        clear.clear()
        chances-=1
        print("welcome to hangman\n")
        dashify(dashes)
        print("that letter is not in the word")
    
if chances>0:
    clear.clear()
    print("welcome to hangman\n")
    dashify(dashes)
    print("\ncongrats! you have won!")
else:
    clear.clear()
    print("welcome to hangman\n")
    dashify(dashes)
    print("\nsorry. you have lost.")
