def isj(n):
    c=0
    for i in range(1,len(n)):
        d=abs(int(n[i])-int(n[i-1]))
        if d==1:
            c+=1
    if c==len(n)-1:
        a=0
    else:
        a=1
    return a
s=int(input())
d=0
for i in range(0,s+1):
    if isj(str(i))==0:
        d+=1
print(d)
