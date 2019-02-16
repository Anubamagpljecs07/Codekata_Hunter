n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,n-1):
    if sum(l[0:i])==sum(l[i+1:n]):
        c+=1
if c>=1:
    print("yes")
else:
    print("no")
