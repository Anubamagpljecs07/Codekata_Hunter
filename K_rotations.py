n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
j=0
for i in range(0,len(l)):
    l.append(l[0])
    l.remove(l[0])
    j+=1
    if l==m:
        print(j)
