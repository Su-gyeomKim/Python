def hgt(n) :
    j=0
    i=0
    if(n==0) :
        print 'notihing'
    if(n>1) :
        while i < n+1 :
            while j < n+1:
                print '*'
                j=j+1
            i=i+1

inp=raw_input()
inp=int(inp)
n=raw_input()
n=int(n)
print 'input :',inp
print 'height :',n

hgt(n)
