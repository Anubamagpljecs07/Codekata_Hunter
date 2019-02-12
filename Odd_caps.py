s=input()
s=list(s)
j=0
g=[]
for i in range(0,len(s)):
    if s[i]!=" ":
        j+=1
    else:
        pass
    if j%2==1:
        g.append(s[i].upper())
    else:
        g.append(s[i])
f=""
for i in g:
    f=f+i
print(f)
