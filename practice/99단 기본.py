print ' Input Number : '
n = raw_input()
n = int(n)

if n>9 :
    print ' wrong input : too high'
if n<1 :
    print ' wrong input : too low'

i=1
if (n>1 and n<10) :  
    while i<10 :
        m = n*i
        print str(n) + '*' + str(i) + '=' + str(m)
        i=i+1
else:
    print ' retry. '


    
