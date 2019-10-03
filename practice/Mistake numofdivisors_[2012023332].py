print'******************************'
print 'Number of divisors'
print'******************************'
print 'Input the first number :'
Fn = raw_input()
print 'Input thesecond number : '
Sn = raw_input()
Fndicount=0
Sndicount=0
i=0
while i<Fn
    if (Fn%i==0)
    Fndicount++
while i<Sn
    if (Sn%i==0)
    Sndicount++
R = Fndicount + Sndicount
print 'Number of divisors of first number is ' + str(Fndicount)
print 'Number of divisors of second number is '+ str(Sndicount++)
print 'Result is :' + str(R)
