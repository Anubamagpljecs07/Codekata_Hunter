s=input()
s=list(s.split(" "))
g=[]
for i in s:
    g.append(i[::-1])
print(*g)
