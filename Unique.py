s=input()
g=[]
for i in s:
	if i not in g:
		g.append(i)
a=""
for i in g:
	a=a+i
print(a)
