s,r=map(str,input().split())
g=""
for i in s:
    if s.count(i)==r.count(i) and i not in g:
        g=g+i
    elif i in r and s.count(i)!=r.count(i) and i not in g:
        d=min(s.count(i),r.count(i))
        for j in range(0,d):
            g=g+i
print(g)
