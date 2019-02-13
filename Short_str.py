s=input()
f=""
i=0
c=1
while(i<=len(s)-1):
	if i<len(s)-1:
		if s[i]==s[i+1]:
			c+=1
		else:
			f=f+str(c)+"*"+s[i]
			c=1
	elif i==len(s)-1:
		f=f+str(c)+"*"+s[i]
		c=1
	
	i=i+1
g=[]
for i in range(0,len(f)):
	if f[i]=="*":
		g.append(f[i-1])
d=0
for i in g:
	d=d+int(i)
if d==len(g):
	print(s)
else:
	print(f)
