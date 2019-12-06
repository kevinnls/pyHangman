class stickman:
    #chances = 6
    stick=['1','2','3','4','5','6','7']
    stick[0] = '''
	
	
	
	••••••••••••••
	'''
    stick[1] = '''
	       o
	
	
	••••••••••••••
	'''
    stick[2] = '''
	       o
	        |
	
	••••••••••••••
	'''
    stick[3] = '''
       	o
	      /|
	
	••••••••••••••
	'''
    stick[4] = '''
       	o
	      /|\\
	
	••••••••••••••
	'''
    stick[5] = '''
       	o
	      /|\\
	        \\
	••••••••••••••
	'''
    stick[6] = '''
       	o
	      /|\\
	       /\\
	••••••••••••••
	'''
    #__init__():
       # pass
        
    def stickout(self, num):
        print(self.stick[num])
        return
man = stickman() 
for i in range(1,7):
    man.stickout(i)