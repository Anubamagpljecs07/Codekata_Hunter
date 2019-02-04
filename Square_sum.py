n=int(input())
g=0
while n>0:
    s=n%10
    g=g+(s*s)
    n=n//10
print(g)
