n,k=map(int,input().split())
l=list(map(int,input().split()))
j=0
for i in range(0,len(l)):
	while j<k:
		l.append(l[0])
		l.remove(l[0])
		j+=1
print(*l)
