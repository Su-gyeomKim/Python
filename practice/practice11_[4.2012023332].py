import random

def findValue(lis,listrange):
    m=lis[0]
    for x in range (0,listrange):
        if (lis[x]>m):
            m=lis[x]
    return m

def findPlace(lis,listrange):
    k=lis[0]
    for x in range (0,listrange):
        if (lis[x]>k):
            k=lis[x]
            K=x
    return K

def count(lis,a,listrange):
    count=0
    for x in range(0,listrange):
        value=lis[x]
        if (value==a):
            count=count+1
    return count

def printLast(a,b,c) :
    print 'The',c,'Maximum number is', a,'and count is', b
    print 'The current length of list is',

lis=[]
for x in range(0,100):
    lis.append(random.randint(1,1000))
print lis
lr=100

for y in range(1,6):
    maxy=findValue(lis,lr)
    county=count(lis,maxy,lr)
    for yy in range(0,county):
        lis.remove(maxy)
    printLast(maxy,county,y)
    lr=lr-county
    print lr

    print max(lis)
    
