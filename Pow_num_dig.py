n=input()
a=len(n)
g=[]
for i in n:
    s=pow(int(i),a)
    g.append(s)
f=0
for i in g:
    f=f+int(i)
print(f)
