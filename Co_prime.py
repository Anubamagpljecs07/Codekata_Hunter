def gcd(n,m):
    x=[]
    for i in range(1,max(n,m)):
        if n%i==0 and m%i==0:
            x.append(i)
    f=len(x)
    return f      
a,b=map(int,input().split())
if gcd(a,b)==1:
    print("yes")
else:
    print("no")
