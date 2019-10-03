def is_right(a, b):
    if len(a) != len(b):
             print 'Not circular identicall'
    else:
        if (a==b):
            print 'Circular string to right 0 times'
            print 'Inverse Circular string to right 0 times'
        if(a!=b):    
            for i in range(0,len(b)):
                if b[0]==a[i]:
                    print 'Circular string to right', i, 'times'
            for i in range(0,len(a)):
                if a[0]==b[i]:
                    print 'Inverse Circular string to right', i, 'times'
            
List= []
List1= []
print "Input First String :"
string=raw_input()
List=list(string)

print "Input second String :"
string1=raw_input()
List1=list(string1)

is_right(List,List1)

