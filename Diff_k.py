n,k=map(int,input().split())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    for j in l:
        if i-j==k:
            c.append(i)
            d.append(j)
print(len(c))
