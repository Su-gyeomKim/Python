i=0
I=1
j=0
k=1
s=0
S=0
def p(I,k,K) :
    print str(I)*k,' + ',str(I)*(k+K),' + '

print "input number :"
i=raw_input()
i=int(i)
print "input length :"
j=raw_input()
j=int(j)

for I in range (1,i+1) :
    K=0
    for k in range (1,j+1) :
        print str(I)*k,' + ' ,
        ##p(I,k,K)
        x=str(I)*k
        x=int(x)
        s=s+x
        k=k+1
        
    
    print '=', s
    S=S+s
    s=0
    k=1  
    I=I+1
    print
print "total Sum =", S
