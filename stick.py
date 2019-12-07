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
	       ᵔ
	••••••••••••••
	'''
    stick[3] = '''
	       o
	      /|
	       ᵔ
	••••••••••••••
	'''
    stick[4] = '''
	       o
	      /|\\
	       ᵔ
	••••••••••••••
	'''
    stick[5] = '''
	       o
	      /|\\
	       ᵔ\\
	••••••••••••••
	'''
    stick[6] = '''
	       o
	      /|\\
	      /ᵔ\\
	••••••••••••••
	'''
    #__init__():
       # pass
        
    def stickout(num):
        print(stickman.stick[6-num])
        return
#man = stickman() 
#for i in range(1,7):
#    stickman.stickout(i)
