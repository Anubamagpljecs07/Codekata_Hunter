n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
	a=l.count(i)
	g.append(a)
m=max(g)
for i in l:
	if l.count(i)==m:
		n=i
		break
print(n)
		
