n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
m=sorted(l,reverse=True)
g=[]
h=[]
i,j=0,0
while i<len(m):
    while j<len(k):
        g.append(m[i])
        g.append(k[j])
        i+=1
        j+=1
a=(0+len(g))//2
for i in range(0,len(g)):
    if i<a:
        h.append(g[i])
print(*h)
