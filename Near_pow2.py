#ganu
def ispow(x):
    for i in range(1,x+1):
        if pow(2,i)==x:
            a=1
            break
        else:
            a=0
    return a
n=int(input())
l=[]
if ispow(n)==1:
    print(0)
else:
    for i in range(1,n):
        if ispow(i)==1:
            l.append(i)
    m=max(l)
    d=n-m
    print(d)
