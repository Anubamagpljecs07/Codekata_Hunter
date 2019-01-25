n=int(input())
l=list(map(int,input().split()))
d={ }
k=[]
for i in l:
    s=l.count(i)
    d.update({i:s})
    k.append(s)
m=max(k)
c=0
for x,y in d.items():
    if c==0:
        if y==m:
            print(x,end="")
            c+=1
    else:   
        if y==m:
            print("",x,end="")
    
