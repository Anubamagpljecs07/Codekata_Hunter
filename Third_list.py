n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
g=[]
for i in range(0,n):
    g.append(l[i]+m[i])
print(*g)
