n=int(input())
c=0
j=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    j+=1
    if n*j in l:
        c+=1
print(c)
