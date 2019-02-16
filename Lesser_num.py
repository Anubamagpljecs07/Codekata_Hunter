n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i<len(l)-1:
        if l[i+1]<l[i] :
            l[i]=l[i+1]
        else:
            a=-1
            l[i]=a
    elif i==len(l)-1:
        a=-1
        l[i]=a
print(*l)
