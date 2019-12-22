import json
from stick import stickman as stickman
from string import ascii_lowercase
#from string import ascii_uppercase
#from string import lower
from random import choice
from clear import clear

def print_dashes(dashes):
    for i in dashes:
        print(i ,end = " ")
    print ("\n")
    
def dashify(raw):
	product=[]
	for i in raw:
		if i not in ascii_lowercase:
			product.append(i)
		else:
			product.append("_")
	return product
			
		
    
def top():
    clear()
    print("welcome to hangman\n \t\t" + "wins: " + str(v) + "   losses: " + str(l))
    stickman.stickout(chances)
    print_dashes(dashes)
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
    print_dashes(dashes)
    print_dashes(word)
    print("clue: " + clue)
    print("\nsorry. you have lost.")
           
### start hangman ###
def hangman():
    cache = []
    global dictionary
    #dictionary = {"a stitch-in-time saves nine!":"quick decisions are fly"}
    global raw_string
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
        while raw_string in completed:
            raw_string,clue = choice(list(dictionary.items()))
        completed.append(raw_string)
    string = list(raw_string)
    dashes = dashify(raw_string)    
    top()
    print("\n")

    while dashes != string and chances>0:
    
        print("used letters: " + str(cache))
        print("chances left: " + str(chances) +"/6")
        guess = input("guess a letter: ")
        guess = guess.lower()
    
    ###tracking used letters###
        #if len(guess)>1:
        #    top()
        #    print("\ntype one letter at a time please\n")
        #    continue
        if len(guess)<1:
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
            for i in guess:
                cache.append(guess)   
    ###tracking used letters###
    
    ###check letter in word###
        for i in guess:
            if i in string:
                n=-1
                for letter in string:
                    n+=1
                    if guess == letter:
                        dashes[n] = string[n]
                top()
                print("\n")
            elif guess not in string:
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

### START of MAIN ###
with open('dictionary.json') as dictf:
        dictionary = json.load(dictf)
        dictf.close()

dashes = ''
clue = ''
raw_string = 'null' 
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
        print("thanks for playing hangman!\n\n total rounds played\t: " + str(v+l) + "\n number of rounds won\t: " + str(v) + "\n number of rounds lost\t: " + str(l) + "\n\nbye bye hope to see you again!")
        exit() 
### END of MAIN ###
