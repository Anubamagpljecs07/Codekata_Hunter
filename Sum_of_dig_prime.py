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
m,n=map(int,input().split())
c=0
for i in range(m,n):
	r=0
	while i!=0:
		g=i%10
		r=r+g
		i=i//10
	if isprime(r)==1:
		if r!=1:
			c+=1
print(c)
			
