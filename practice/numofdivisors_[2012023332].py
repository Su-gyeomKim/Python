print'******************************'
print 'Number of divisors'
print'******************************'
print 'Input the first number :'
Fn = raw_input()
Fn= int(Fn)
print 'Input thesecond number : '
Sn = raw_input()
Sn=int(Sn)
Fncount=0
Sncount=0
i=1
while Fn>=i :
    
    if (Fn%i==0):
        Fncount = Fncount+1
    i=i+1
i=1
while Sn>=i :
    
    if (Sn%i==0):
        Sncount = Sncount+1
    i=i+1
R = Fncount + Sncount
print 'Number of divisors of first number is ' + str(Fncount)
print 'Number of divisors of second number is '+ str(Sncount)
print 'Result is :' + str(R)
