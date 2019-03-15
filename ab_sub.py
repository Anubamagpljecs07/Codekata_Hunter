s=input()
g=""
l=[]
c=0
for i in range(0,len(s)):
	if c%2==0:
		if s[i]=="a":
			g=g+s[i]
			c+=1
		else:
			l.append(g)
			g=""
			c=0
	else:
		if s[i]=="b":
			g=g+s[i]
			c+=1
		else:
			l.append(g)
			g=""
			c=0
	if i==len(s)-1:
		l.append(g)
a=[]
for i in l:
	a.append(len(i))
m=max(a)
print(m)
