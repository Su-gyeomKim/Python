def multip(n,i,m) :
    if (n>1 and n<10) :  
        while i<10 :
            m = n*i
            print str(n) + '*' + str(i) + '=' + str(m)
            i = i+1
    else :
        print ' retry. '
        n = raw_input()
        n = int(n)
        multip(n,i,m)    
print ' Input Number : '
n = raw_input()
n = int(n)
m=0
i=1
if n>9 :
    print ' too high '
if n<1 :
    print ' too low'

if (n>1 and n<10) :
    print'**********' + str(n) + 'times table**********'
    multip(n,i,m)
    print'*********************************'
