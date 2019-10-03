def fib(n) :
     if n == 1 or n == 2 :
         return 1;
         return fib(n - 1) + fib(n - 2)

while(1):
    print '***********'
    print '1.Calculate'
    print '2.Show it!'
    print '3.Initialize'
    print '4.Quit'
    print '***********'

    a=int(raw_input)
    if (a==1):
        print'input:',a
        print 'Input first number:'
        f1=int(raw_input)
        print 'Input Second number:'
        f2=int(raw_input)
        print 'Input number:',
        total=int(raw_input)
    if(a==2):
        for x in range(1,total):
            print fib(x)
    if (a==3):
        f1=0
        f2=1
    if(a==4):
        return 0;
