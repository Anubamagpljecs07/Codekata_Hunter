from itertools import permutations
s=input()
a=len(s)
c=0
if a%2==0:
	print("NO")
else:
	l=list(permutations(s,a-1))
	g=[]
	f=""
	for i in l:
		for j in i:
			f=f+j
		g.append(f)
		f=""
	for i in g:
		for j in range(len(i)):
			if i[j:(a-1)//2]==i[(a-1)//2:]:
				c+=1
if c==0:
	print("NO")
else:
	print("YES")
