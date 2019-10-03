def fib(n,f1,f2) :
    
    if n == 1 :
        return f1
    if n == 2 :
        return f2
    else:
        return fib(n-1,f1,f2) + fib(n - 2,f1,f2)

while(1):
    print '***********'
    print '1.Calculate'
    print '2.Show it!'
    print '3.Initialize'
    print '4.Quit'
    print '***********'
    
    a=int(raw_input())
    if (a==1):
        print'input:',a
        print 'Input first number:'
        f1=int(raw_input())
        print 'Input Second number:'
        f2=int(raw_input())
        print 'Input number:',
        total=int(raw_input())
    if(a==2):
        for x in range(1,total+2):
            print fib(x,f1,f2),
        print
    if (a==3):
        f1=0
        f2=1
        total=1
    if(a==4):
        break;
