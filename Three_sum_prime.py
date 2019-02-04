def isprime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c+=1
    if c==0:
        a=0
    else:
        a=1
    return a
n=int(input())
g=[]
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if i+j+k==n:
                if isprime(i)==0 and isprime(j)==0 and isprime(k)==0 and i!=1 and j!=1 and k!=1:
                    if i not in g and j not in g and k not in g:
                        g.append(i)
                        g.append(j)
                        g.append(k)
g=sorted(g)
h=[]
c=0
if len(g)>3:
    while c<2:
        m=min(g)
        h.append(m)
        g.remove(m)
        c+=1
s=0
for i in h:
    s=s+i
for i in g:
    if i+s==n:
        h.append(i)
print(*h)
