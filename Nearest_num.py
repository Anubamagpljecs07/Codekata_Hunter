n,k=map(int,input().split())
l=list(map(int,input().split()))
g,a=[],[]
for i in l:
	if i!=k:
		f=abs(i-k)
		g.append(f)
g=sorted(g)
for i in range(0,3):
	for j in l:
		if abs(j-k)==g[i] and j not in a:
			a.append(j)
print(*a)
