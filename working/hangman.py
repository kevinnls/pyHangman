### this is the Hangman class
import json
from stick import stickman as stickman
from string import ascii_lowercase as letters
from random import choice
from clear import clear


class Hangman:
    def __init__(self):        
        self.dashes = ''
        self.clue = ''
        self.raw_string = '\0' 
        self.completed = ['\0']
        self.tried_letters = []
        self.chances = 6
        self.v = 0
        self.l = 0
        self.how_to_play='''
            guess letters till you find the word in question. 
                can you find the answer and escape the gallows?
    
            for each letter that isn't in the word, 
                another part of you is hung.
               
            you may guess multiple letters at a time,
                but how sure are you of the answer...?
    
            remember. your life dangles on the string.'''
        #defining dictionary#
        with open('dictionary.json') as dictf:
                self.dictionary = json.load(dictf)
                dictf.close()
        self.main_menu()
                
    def check(self, char, string):
        if char in string:
            n=-1
            for letter in string:
                n+=1
                if char == letter:
                    self.dashes[n] = string[n]
            return 0
        elif char not in string:
            return 1
            
    def print_dashes(self, dashes):
        print("   ", end= "")
        for i in dashes:
            print(i, end = " ")
        print ("\n")
        
    def dashify(self, raw):
        product=[]
        for i in raw:
            if i not in letters:
                product.append(i)
            else:
                product.append("_")
        return product
        
    def top(self):
        clear()
        print("welcome to hangman\n \t\t" + "wins: " + str(self.v) + "   losses: " + str(self.l))
        stickman.stickout(self.chances)
        self.print_dashes(self.dashes)
        print("clue: " + self.clue +"\n")
        return
    
    def top_win(self):
        self.v += 1
        self.top()
        print("\ncongrats! you have won!")
        
    def top_loss(self):
        self.l += 1
        clear()
        print("welcome to hangman\n \t\t" + "wins: " + str(self.v) + "   losses: " + str(self.l))
        stickman.stickout(0)
        self.print_dashes(self.dashes)
        self.print_dashes(self.raw_string)
        print("clue: " + self.clue)
        print("\nsorry. you have lost.")
               
    ### start hangman ###
    def hangman(self):
        ### INIT START###
        #loading attributes#
         # dictionary
        # #dictionary = {"a stitch-in-time saves nine!":"quick decisions are fly"}
        # global raw_string
        # global clue
        # global dashes
        # global completed
        # global chances
        # global l
        # global v
        self.tried_letters = []
        self.chances = 6
        
        #check if dictionary exhausted#
        if len(self.completed) == len(self.dictionary)+1:
           clear() 
           print("thank you for playing hangman\n")
           print("you have beat the game. our dictionary has been exhausted.\n\nyou won " + str(v) + " times\nand lost " + str(l) + " times\n\ncongrats!")
           exit()
        #load unused raw_string from dictionary#	
        else:	
            while self.raw_string in self.completed:
                self.raw_string,self.clue = choice(list(self.dictionary.items()))
            self.completed.append(self.raw_string)
            
        #dashify the raw_string and convert it to list of characters
        self.string = list(self.raw_string)
        self.dashes = self.dashify(self.raw_string)
        ### INIT END ###
            
        self.top()
        while self.chances > 0 and self.dashes != self.string:
        
            print("\ntried letters: " + str(self.tried_letters))
            print("body parts left: " + str(self.chances) +"/6")
            self.guess = input("\n what's your guess? ")
            self.guess = list(dict.fromkeys(list(self.guess.lower())))
            
            if len(self.guess)<1:
                self.top()
                continue
            else:
                usedchar = []
                wrongchar = []
                notchar = 0
                for char in self.guess:
                    if char not in letters:
                        notchar+=1
                    elif char in letters and char in self.tried_letters:
                        usedchar.append(char)
                    elif char in letters and char not in self.tried_letters:
                        self.tried_letters.append(char)
                        result=self.check(char, self.string)
                        if result == 0 and self.dashes == self.string:
                            break
                        if result == 1:
                            wrongchar.append(char)
                            self.chances-=1
                self.top()
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
    
        if self.chances>0:
            self.top_win()
            return
        else:
            self.top_loss()
            return
    ### end hangman() ###
    
    def main_menu(self):
        clear()
        print("welcome to hangman\n")
        print(self.how_to_play)
        start = input("press enter to play. \nif you want to quit enter q. \n :")
        if start == 'q':
            clear()
            print("thanks for stopping by at hangman\n\nbye! bye!")
            exit()
        else:
            self.main_game()
            
    def main_game(self):    
        while True:
            self.hangman()
            
            inp = input("\nwould you like to play again? y/n: ").lower()
            while inp != 'y' and inp != 'n':
                clear()
                print("welcome to hangman\n")
                stickman.stickout(6)
                inp = input("\ninvalid choice. \nwould you like to play again? press y/n: ").lower()
            if inp == 'y':
                continue
            elif inp == 'n':
                clear()
                
                print("thanks for playing hangman!\n")
                stickman.stickout(6)
                print("\n total rounds played\t: " + str(self.v+self.l) + "\n number of rounds won\t: " + str(self.v) + "\n number of rounds lost\t: " + str(self.l) + "\n\nbye bye hope to see you again!")
                exit()        
    

player1 = Hangman()
