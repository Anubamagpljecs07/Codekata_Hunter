n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
if len(k)>len(l):
    print("NO")
else:
    for i in k:
        if i in l:
            c+=1
    if c==len(k):
        print("YES")
    else:
        print("NO")
            
