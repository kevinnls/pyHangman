import json
from stick import stickman as stickman
from string import ascii_lowercase as letters
from random import choice
from clear import clear

### global attributes ###
dashes = ''
clue = ''
raw_string = '\0' 
completed = ['\0']
chances = 0
v = 0
l = 0
#defining dictionary#
with open('dictionary.json') as dictf:
        dictionary = json.load(dictf)
        dictf.close()
def verify(char, string):
    global dashes
    if char in string:
        n=-1
        for letter in string:
            n+=1
            if char == letter:
                dashes[n] = string[n]
        return 0
    elif char not in string:
        return 1
def print_dashes(dashes):
    print("   ", end= "")
    for i in dashes:
        print(i, end = " ")
    print ("\n")
    
def dashify(raw):
	product=[]
	for i in raw:
		if i not in letters:
			product.append(i)
		else:
			product.append("_")
	return product
    
def top():
    clear()
    print("welcome to hangman\n \t\t" + "wins: " + str(v) + "   losses: " + str(l))
    stickman.stickout(chances)
    print_dashes(dashes)
    print("clue: " + clue +"\n")
    return

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
    stickman.stickout(0)
    print_dashes(dashes)
    print_dashes(raw_string)
    print("clue: " + clue)
    print("\nsorry. you have lost.")
           
### start hangman ###
def hangman():
    ### INIT START###
    #loading attributes#
    global dictionary
    #dictionary = {"a stitch-in-time saves nine!":"quick decisions are fly"}
    global raw_string
    global clue
    global dashes
    global completed
    global chances
    global l
    global v
    tried_letters = []
    chances = 6   
    
    #check if dictionary exhausted#
    if len(completed) == len(dictionary)+1:
       clear() 
       print("thank you for playing hangman\n")
       print("you have beat the game. our dictionary has been exhausted.\n\nyou won " + str(v) + " times\nand lost " + str(l) + " times\n\ncongrats!")
       exit()
    #load unused raw_string from dictionary#	
    else:	
        while raw_string in completed:
            raw_string,clue = choice(list(dictionary.items()))
        completed.append(raw_string)
        
    #dashify the raw_string and convert it to list of characters
    string = list(raw_string)
    dashes = dashify(raw_string)
    ### INIT END ###
        
    top()
    while dashes != string and chances>0:
    
        print("\ntried letters: " + str(tried_letters))
        print("body parts left: " + str(chances) +"/6")
        guess = input("\n what's your guess? ")
        guess = guess.lower()
        
        if len(guess)<1:
            top()
            continue
        else:
            usedchar = []
            wrongchar = []
            notchar = 0
            for char in guess:
                if char not in letters:
                    notchar+=1
                elif char in letters and char in tried_letters:
                    usedchar.append(char)
                elif char in letters and char not in tried_letters:
                    tried_letters.append(char)
                    result=verify(char, string)
                    if result == 0 and dashes == string:
                        break
                    if result == 1:
                        wrongchar.append(char)
                        chances-=1
            top()
            if len(wrongchar)==1:
                print("  the letter " + str(wrongchar) + " is not in the word")
            if len(wrongchar)>1:
                print("  the letters " + str(wrongchar) + " are not in the word")
            if len(usedchar)==1:
                print("  you have already tried the letter " + str(usedchar))
            elif len(usedchar)>1:
                print("  you have already tried the letters " + str(usedchar))
            if notchar>0:
                print("  please type only letters")
            pass

    if chances>0:
        top_win()
        return
    else:
        top_loss()
        return
### end hangman() ###

### START of MAIN ###
clear()
print("welcome to hangman\n")
print('''
        guess letters till you find the word in question. 
            can you find the answer and escape the gallows?

        for each letter that isn't in the word, 
            another part of you is hung.
           
        you may guess multiple letters at a time,
            but how sure are you of the answer...?

        remember. your life dangles on the string.

''')
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
