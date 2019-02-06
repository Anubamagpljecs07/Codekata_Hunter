n=int(input())
m=input()
s=list(m.split(" "))
g=[]
for i in s:
    a=i.casefold()
    g.append(a)
g=sorted(g)
for i in range(0,len(g)):
    if i!=len(g)-1:
        print(g[i])
    else:
        print(g[i])
