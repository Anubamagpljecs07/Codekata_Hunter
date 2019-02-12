def isprime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            a=0
            c+=1
    if c==0:
        a=1
    return a
n=int(input())
g=[]
for i in range(1,n):
    if isprime(i)==1 and i!=1:
        g.append(i)
g=sorted(g)
if len(g)!=0:
    print(*g)
else:
    print(0)
