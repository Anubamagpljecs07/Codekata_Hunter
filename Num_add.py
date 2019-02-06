n=input()
g=list(n)
s=[]
a=0
for i in range(0,len(g)):
    if i==0:
        s.append(g[i])
    else:
            a=int(g[i])+int(s[i-1])
            s.append(a)
f=0
for i in range(0,len(s)):
    f=f+int(s[i])
print(f)
