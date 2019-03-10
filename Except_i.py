n=int(input())
l=list(map(int,input().split()))
g=[]
for i in range(len(l)):
	a=1
	for j in range(len(l)):
		if j!=i:
			a=a*l[j]
	g.append(a)
print(*g)
