n=int(input())
l=[]
g=[]
for i in range(0,n):
    l.append(input().split())
for i in range(0,len(l)):
    x=n-i-1
    g.append(int(l[i][x]))
print(sum(g))
