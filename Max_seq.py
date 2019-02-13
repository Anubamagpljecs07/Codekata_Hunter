s=input()
f=""
i,c=0,1
g=[]
while i<=len(s)-1:
    if i<len(s)-1:
        if s[i]==s[i+1]:
            c+=1
        else:
            g.append(s[i])
            g.append(c)
            c=1
    else:
        g.append(s[i])
        g.append(c)
    i+=1
a=[]
for i in g:
    if str(i).isdigit():
        a.append(i)
m=max(a)
for i in range(0,len(g)):
    if g[i]==m:
        print(g[i-1],m)
        
