m,n=map(str,input().split())
n=int(n)
g=[]
for i in range(0,len(m)-n+1):
	g.append(m[i:i+n])
print(*g)
