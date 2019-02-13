n=int(input())
l=list(map(int,input().split()))
m=min(l)
n=max(l)
g=[]
h=[]
for i in range(0,len(l)):
    if l[i]==m:
        g.append(i+1)
    elif l[i]==n:
        h.append(i+1)
f=[]
for i in g:
    f.append(i)
for i in h:
    f.append(i)
print(*f)
    
