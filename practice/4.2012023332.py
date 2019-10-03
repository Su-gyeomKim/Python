def hgt(n) :
    j=1
    i=1
    s='*'
    if(n==0) :
        print 'notihing'
    else :
        print('')
        while (i < n)or(i==n) :
            print '*'*i
            i=i+1
            
            

n = raw_input()
n = int(n)
print 'Height :', n
hgt(n)
