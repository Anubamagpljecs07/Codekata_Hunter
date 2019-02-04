def isprime(x):
	c=0
	for i in range(2,x):
		c+=1
	if c==0:
		a=1
	else:
		a=0
	return a
n=int(input())
g=[]
for i in range(2,n+1):
	print(i)
	if isprime(i)==1:
		print(i)
		a=str(i)
		print(a)
		if a[-1]==3:
			print(i)
			g.append(i)
			print(g)
s=0
for i in g:
	s=s+i
print(s)
	
