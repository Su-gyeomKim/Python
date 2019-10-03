def DivisorCount(Fn) :
    i=1
    Fncount = 0
    while Fn>=i :
        if (Fn%i==0):
            Fncount = Fncount+1
        i=i+1
    return Fncount

print'******************************'
print 'Number of divisors'
print'******************************'
print 'Input the first number :'
Fn = raw_input()
Fn= int(Fn)
print 'Input thesecond number : '
Sn = raw_input()
Sn = int(Sn)
DivisorCount(Fn)
DivisorCount(Sn)
R=DivisorCount(Fn)+DivisorCount(Sn)

print 'Number of divisors of first number is ' + str(DivisorCount(Fn))
print 'Number of divisors of second number is '+ str(DivisorCount(Fn))
print 'Result is :' + str(R)
