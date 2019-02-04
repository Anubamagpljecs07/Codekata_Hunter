def isprime(x):
	c=0
	for i in range(2,x):
		if x%i==0:
			c+=1
	if c==0:
		a=1
	else:
		a=0
	return a
n=int(input())
g=[]
for i in range(2,n+1):
	c=isprime(i)
	if c==1:
		a=str(i)
		if a[-1]=="3":
			g.append(i)
s=0
for i in g:
	s=s+i
print(s)
	
