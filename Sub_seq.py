s=input()
r=input()
g=""
if len(s)>=len(r):
    for i in range(0,len(s)):
        for j in range(0,len(r)):
            if s[i]==r[j] and i>=j  and r[j] not in g:
                g=g+r[j]
else:
    for i in range(0,len(s)):
        for j in range(0,len(r)):
            if s[i]==r[j] and i<=j  and r[j] not in g:
                g=g+r[j]
print(g)
