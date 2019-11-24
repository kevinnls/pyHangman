from time import sleep as sleep
sleep(2)
print ("hello world\n")

para = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In pretium, arcu vitae imperdiet sagittis, risus urna tempus ipsum, id sagittis leo felis et tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tristique fermentum tristique. Nulla mattis aliquam augue. Maecenas nunc est, condimentum ut fermentum et, venenatis quis magna. Aliquam vitae turpis bibendum, sodales massa at, interdum eros. Cras a diam velit. Integer malesuada libero ut nisi tempus, varius cursus nisl volutpat.
Nullam sollicitudin massa vel est mattis vestibulum. Nunc fringilla orci sed erat mattis, vitae tempus ex pulvinar. In mollis augue at nisl condimentum volutpat. Fusce luctus hendrerit est sed convallis. Mauris condimentum luctus tristique. Pellentesque elit arcu, luctus a erat a, tincidunt ultricies felis. Aliquam facilisis odio eu pulvinar condimentum. Nulla facilisi. Integer fermentum nulla in gravida tincidunt.'''

buff = "\t"
#ncols = 0
for i in para:
    if i == ' ':
        print(buff, end='')
        buff = " "
        sleep(0.05)
        continue
    elif i == '\n':
        print(buff)
        buff = "\n\t"
        continue
    else:
        buff += i
        #ncols +=1
        #print(buff)
        continue
        
