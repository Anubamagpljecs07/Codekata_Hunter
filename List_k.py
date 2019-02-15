n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if i!=j:
			if l[i]+l[j]==k:
				c+=1
if c>=1:
	print("YES")
else:
	print("NO")
