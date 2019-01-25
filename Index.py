n=input()
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    if i==l[i]:
        c+=1
        if c==1:
            print(i,end="")
        else:
            print("",i,end="")
if c==0:
    print("-1")
