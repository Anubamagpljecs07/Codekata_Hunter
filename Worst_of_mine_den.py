n=int(input())
n1=n
g=[]
n=n//1000
g.append(n)
n=n1%1000
n1=n
n=n//500
g.append(n)
n=n1%500
n1=n
n=n//100
g.append(n)
n=n1%100
n1=n
n=n//50
g.append(n)
n=n1%50
n1=n
n=n//10
g.append(n)
n=n1%10
n1=n
n=n//1
g.append(n)
a=0
for i in g:
	a=a+i
print(a)
