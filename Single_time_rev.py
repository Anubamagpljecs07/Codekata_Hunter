s=input()
g=""
for i in s:
	if i not in g:
		g=g+i
print(g[::-1])
