def q(a):
    
    c=0
    b=raw_input()
    int(b)
    
    c=c+b
    return c

def guessOfComputer(start, end):
    b=0
    b=int((start+end)/2)
    return int(b)


print'******************************'
print 'Reversed guess the number'
print'******************************'
print 'what number are you thinking about? (1 to 100)'
n=raw_input()
n=int(n)

s=1
e =100
print 'Input the interval :'
i=raw_input()
i=int(i)

print 'start'

def all (s,e):
    print 'guess is', guessOfComputer(s,e)
    b=guessOfComputer(s,e) 
    b=int(b)
    ii=0
    ii=ii+1
    c=0
    c=c+int(b)


    if (b>n) :
        print'big'
        e=b
        ii=ii+1
        c=c+int(b)
        
    if (b<n) :
        print'small'
        s=b
        ii=ii+1
        c=c+int(b)
    return ii

def alll (s,e):
    print 'guess is', guessOfComputer(s,e)
    b=guessOfComputer(s,e) 
    b=int(b)
    ii=0
    ii=ii+1
    c=0
    c=c+int(b)


    if (b>n) :
        print'big'
        e=b
        ii=ii+1
        c=c+int(b)
        
    if (b<n) :
        print'small'
        s=b
        ii=ii+1
        c=c+int(b)
    return c

if(b==n) :
    print 'you get the guess!!'
    print 'The number of the computers guess is',all(s,e)
    print 'total Sum is'
    print alll(s,e)
