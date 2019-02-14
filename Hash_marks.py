a=input()
b=input()
a=list(a.split("#"))
b=list(b.split("#"))
g,h=[],[]
for i in range(1,len(a)):
	g.append(int(a[i]))
for i in range(1,len(b)):
	h.append(int(b[i]))
c=sum(g)
d=sum(h)
if d>c:
	print(b[0])
if c>d:
	print(a[0])
