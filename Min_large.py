from itertools import permutations
s=str(input())
l=list(permutations(s))
g=[]
a=""
for i in l:
	for j in i:
		a=a+j
	g.append(int(a))
	#print(g)
	a=""
g.remove(int(s))
#print(g)
f=[]
for i in g:
	if i>int(s):
		f.append(i)
#print(f)
if f!=[]:
	m=min(f)
	print(m)
else:
	print("impossible")
