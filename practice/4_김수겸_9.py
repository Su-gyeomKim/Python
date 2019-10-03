def Incr(n) :
    i=1
    s='*'
    if(n==0) :
        print 'notihing'
    else :
        while (i < n)or(i==n) :
            print '*'*i
            i=i+1
def Decr(n) :
    i=n
    s='*'
    if(n==0) :
        print 'notihing'
    else :
        while (i!=0):
            print '*'*i
            i=i-1                   
            
Input = raw_input()
Input=int(Input)
hgt = raw_input()
hgt = int(hgt)
Times=0
print 'Input :', Input
print 'Height :', hgt
if Input==1:
    Incr (hgt)
elif Input==2:
    Decr(hgt)
elif Input==3:
    Incr (hgt)
    Decr(hgt-1)
elif Input==4:
    while(Times<10):
        Incr (hgt)
        Decr(hgt-1)
        Times=Times+1
        print 'Times :', Times
