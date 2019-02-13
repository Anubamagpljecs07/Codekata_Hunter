n=int(input())
l=list(map(int,input().split()))
u,v=map(int,input().split())
g,h,d=[],[],[]
for i in range(0,len(l)):
    if l[i]==u:
        g.append(i)
    elif l[i]==v:
        h.append(i)
for i in g:
    for j in h:
        f=abs(i-j)
        d.append(f)
m=min(d)
print(m)
