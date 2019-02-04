n=int(input())
l=list(map(int,input().split()))
g=0
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if i<j and l[i]<l[j]:
            g+=1
print(g)
