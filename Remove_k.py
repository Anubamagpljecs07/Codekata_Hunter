n,k=map(int,input().split())
l=list(map(int,input().split()))
a=l.count(k)
for i in range(0,a):
	l.remove(k)
if len(l)>0:
	print(*l)
else:
	print("empty")
