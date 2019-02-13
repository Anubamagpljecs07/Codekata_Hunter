#g
s=input()
f=""
i,c=0,1
while i<=len(s)-1:
    if i<len(s)-1:
        if s[i]==s[i+1]:
            c+=1
        else:
            if c!=1:
                f=f+str(c)+"*"+s[i]
                c=1
            else:
                f=f+s[i]
                c=1
    elif i==len(s)-1:
        if c!=1:
            f=f+str(c)+"*"+s[i]
            c=1
        else:
            f=f+s[i]
            c=1
    i=i+1
print(f)
