n=input()
a=[]
for i in range(0,len(n)):
    if i!=len(n)-1:
        g=pow(int(n[i]),int(n[i+1]))
        a.append(g)
    else:
        g=pow(int(n[i]),int(n[0]))
        a.append(g)
s=0
for i in a:
    s=s+int(i)
print(s)
