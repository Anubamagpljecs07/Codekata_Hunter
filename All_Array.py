n,k=map(int,input().split())
l=[]
for i in range(0,n):
    l.append(input().split())
m=l[0]
n=len(m)
for i in range(0,len(l)):
    j=0
    while j <len(m):
        if m[j] not in l[i]:
            del m[j]
            j-=1
        j+=1
m=sorted(m)
print(*m)
