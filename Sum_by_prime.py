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
h=[]
for i in range(1,n):
    for j in range(1,n):
        if i+j==n:
            if isprime(i)==0 and isprime(j)==0:
                if i not in h and i!=1:
                    g.append(i)
                if j not in g and j!=1:
                    h.append(j)
print(len(g))
