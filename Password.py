r,s=map(str,input().split())
r=list(r)
s=list(s)
a=len(r)
b=len(s)
g=""
if a<b:
    for i in range(1,(b-a)+1):
        r.append(i)
else:
    for i in range(1,(a-b)+1):
        s.append(i)
for i in range(0,len(r)):
    for j in range(0,len(s)):
        if i==j:
            g=g+str(r[i])
            g=g+str(s[j])
print(g)
        
