def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        a=1
    else:
        a=0
    return a
a,b=map(int,input().split())
d=0
for i in range(a,b+1):
    g=bin(i)
    c=g.count("1")
    if prime(c)==1 and c!=1:
        d+=1
print(d)
