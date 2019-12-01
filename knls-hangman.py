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
def top():
    clear()
    print("welcome to hangman\n")
    print(word + clue)
    print(completed)
    dashify(dashes)
    print("clue: " + clue)
def top_loss():
    clear()
    print("welcome to hangman\n")
    dashify(dashes)
    dashify(word)
    print("clue: " + clue)

def hangman():
    letters = []
    global dictionary
    global word
    global clue
    global dashes
    global completed
    chances = 6   
    while word in completed:
        pick = choice(list(dictionary.items()))
        word = pick[0]
        clue = pick[1]
    completed.append(word)
    wordx = listify(word)
    dashes = listify("_" * len(word))
    
    top()
    print("\n")

    while dashes != wordx and chances>0:
    
        print("used letters: " + str(letters))
        print("chances left " + str(chances) +"/6")
        guess = input("guess a letter: ")
    
    ###tracking used letters###
        if len(guess)>1 or guess == '' :
            top()
            print("\ntype one letter at a time please\n")
            continue
        elif guess in letters:
            top()
            print("\nthis letter has already been used\n")
            continue
        elif guess not in letters:
            letters.append(guess)   
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
        top()
        print("\ncongrats! you have won!")
    else:
        top_loss()
        print("\nsorry. you have lost.")


with open('dictionary.json') as dictf:
        dictionary = json.load(dictf)
        dictf.close()
dashes = ''
clue = ''
word = 'null'
completed = ['null']
while True:
    hangman()
    print(word + clue)
    choice = input("wanna play again? y/n: ")
    if choice == 'y':
        hangman()     
    elif choice == 'n':
        print("thanks! bye bye!")
        exit()
    else:
        print("invalid choice")         
