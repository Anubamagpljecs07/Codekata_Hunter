n=int(input())
l=list(map(int,input().split()))
m=min(l)
g=[]
c,i=0,0
while i<len(l):
    if str(l[i])!=str(m) and c==0:
        l.remove(l[0])
        i-=1
    elif l[i]==m:
        c+=1
    i+=1
n=max(l)
print(n-m)
