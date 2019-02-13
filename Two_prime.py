def isprime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c+=1
    if c==0:
        a=0
    else:
        a=1
    return a
n=int(input())
g=[]
h=[]
for i in range(2,n):
    for j in range(2,n):
        if i+j==n:
            if isprime(i)==0 and isprime(j)==0:
                if i not in h:
                    g.append(i)
                if j not in g:
                    h.append(j)
f=[]
if len(g)>1:
	if min(g)<min(h):
		f.append(min(g))
		for i in h:
			if min(g)+i==n:
				f.append(i)
	else:
		f.append(min(h))
		for i in g:
			if min(h)+i==n:
				f.append(i)
else:
	f.append(g[-1])
	f.append(h[-1])
print(*f)		
	
