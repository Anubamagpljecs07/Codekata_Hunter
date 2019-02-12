n,k=map(int,input().split())
l=[]
for i in range(0,n):
    l.append(input().split())
m=l[0]
for i in l:
    for j in m:
        if j not in i:
            m.remove(j)
print(*m)

