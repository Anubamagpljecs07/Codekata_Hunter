n=int(input())
l=list(map(str,input().split()))
u=input()
a=len(u)
c=0
for i in l:
    if i[0:a]==u:
        c+=1
print(c)
