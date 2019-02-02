s=input()
l=list(s.split())
c=0
for i in l:
    if i[0].isupper():
        c+=1
if c==len(l):
    print("yes")
else:
    print("no")
