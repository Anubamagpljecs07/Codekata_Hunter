n=int(input())
l=list(map(str,input().split()))
a=l[::-1]
g=""
for i in range(0,len(a)):
	if i<len(a)-1:
		g=g+a[i]
		g=g+"->"
	else:
		g=g+a[i]
print(g)
