n=int(input())
g=[]
for i in range(n):
    g.append(input())
h=[]
for i in g:
    for j in i:
        if j!=" ":
            h.append(j)
s=0
for i in h:
    s=s+int(i)
a=s/len(h)
g=round(a,5)
g=str(g)
c=0
for i in range(len(g)):
    if g[i]==".":
        a=len(g)-1-i
        if a<5:
            for i in range(5-a):
                g=g+'0'
print(g)
