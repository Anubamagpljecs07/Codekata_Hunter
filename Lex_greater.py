s=input()
s=list(s)
a=ord(s[0])
b=len(s)
c=0
g=""
for i in range(0,b):
    if ord(s[i])<=a and c==0:
        pass
    elif ord(s[i])>a or c>=1:
        c+=1
        g=g+s[i]
print(g)
