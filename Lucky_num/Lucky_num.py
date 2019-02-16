n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if n*i in l:
        c+=1
print(c)
