s=input()
s=list(s.split(" "))
g=[]
for i in range(0,len(s)):
    if i%2==0:
        g.append(s[i][::-1])
    else:
        g.append(s[i])
print(*g)
