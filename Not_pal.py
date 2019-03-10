a=input()
a=list(a)
if a==a[::-1]:
	while a==a[::-1]:
		a[-1]=""
g=""
for i in a:
	g=g+i
print(g)
