n=str(input())
g=[]
i,j=0,0
while i<len(n):
    while j<len(n):
        a=pow(int(n[i]),j)
        g.append(a)
        i+=1
        j+=1
s=0
for i in g:
    s=s+i
print(s)
