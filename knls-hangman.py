import json
from stick import stickman
from string import ascii_lowercase
#from string import ascii_uppercase
#from string import lower
from random import choice
from clear import clear

def dashify(dashes):
    for i in dashes:
        print(i ,end = " ")
    print ("\n")
    
def top():
    clear()
    print("welcome to hangman\n \t\t" + "wins: " + str(v) + "   losses: " + str(l))
    stickman.stickout(chances)
    dashify(dashes)
    print("clue: " + clue)
    
def top_win():
    global v
    v += 1
    top()
    print("\ncongrats! you have won!")
    
def top_loss():
    global l
    l += 1
    clear()
    print("welcome to hangman\n \t\t" + "wins: " + str(v) + "   losses: " + str(l))
    stickman.stickout(chances)
    dashify(dashes)
    dashify(word)
    print("clue: " + clue)
    print("\nsorry. you have lost.")
           
### start hangman ###
def hangman():
    cache = []
    global dictionary
    global word
    global clue
    global dashes
    global completed
    global chances
    global l
    global v
    chances = 6   
    
    if len(completed) == len(dictionary)+1:
       clear()
       print("thank you for playing hangman\n")
       print("you have beat the game. our dictionary has been exhausted.\n\nyou won " + str(v) + " times\nand lost " + str(l) + " times\n\ncongrats!")
       exit()
    	
    else:	
        while word in completed:
            pick = choice(list(dictionary.items()))
            word = pick[0]
            clue = pick[1]
            del pick
        completed.append(word)
    wordx = list(word)
    dashes = list("_" * len(word))    
    top()
    print("\n")

    while dashes != wordx and chances>0:
    
        print("used letters: " + str(cache))
        print("chances left: " + str(chances) +"/6")
        guess = input("guess a letter: ")
        guess = guess.lower()
    
    ###tracking used letters###
        if len(guess)>1:
            top()
            print("\ntype one letter at a time please\n")
            continue
        elif len(guess)<1:
            top()
            print("\n type at least one letter please\n")
            continue
        elif guess not in list(ascii_lowercase):
            top()
            print("\ntype only letters please\n")
            continue
        elif guess in cache:
            top()
            print("\nthis letter has already been used\n")
            continue
        elif guess not in cache:
            cache.append(guess)   
    ###tracking used letters###
    
    ###check letter in word###
        if guess in wordx:
            n=-1
            for i in wordx:
                n+=1
                if guess == i:
                    dashes[n] = wordx[n]
            top()
            print("\n")
         
        elif guess not in wordx:
            chances-=1
            top()
            print("\nthat letter is not in the word\n")
    
    if chances>0:
        top_win()
        return
    else:
        top_loss()
        
        return
### end hangman() ###

with open('dictionary.json') as dictf:
        dictionary = json.load(dictf)
        dictf.close()



### START of MAIN ###
dashes = ''
clue = ''
word = 'null' 
completed = ['null']
chances = 0
v = 0
l = 0

clear()
print("welcome to hangman\n")
start = input("press enter to play. \nif you want to quit enter q. \n :")
if start == 'q':
    clear()
    print("thanks for stopping by at hangman\n\nbye! bye!")
    exit()
else:
    pass
while True:
    hangman()
    inp = input("\nwould you like to play again? y/n: ").lower()
    while inp != 'y' and inp != 'n':
        if chances > 0:
            #top()
            clear()
            print("welcome to hangman")
        else:
            #top_loss()    
            clear()
            print("welcome to hangman")
        inp = input("\ninvalid choice. \nwould you like to play again? press y/n: ").lower()
    if inp == 'y':
        continue
    elif inp == 'n':
        clear()
        print("thanks for playing hangman!\n\nyou won " + str(v) + " times\nand lost " + str(l) + " times\n\nbye bye hope to see you again!")
        exit() 
### END of MAIN ###
