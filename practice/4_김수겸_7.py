def Incr(n) :
    i=1
    s='*'
    if(n==0) :
        print 'notihing'
    else :
        while (i < n)or(i==n) :
            print '*'*i
            i=i+1
            
hgt = raw_input()
hgt = int(hgt)
print 'Height :', hgt
Incr (hgt)
