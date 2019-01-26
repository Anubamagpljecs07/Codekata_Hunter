#ganu
n=int(input())
x=[i for i in input().split()]
d=[]
c=0
for i in range(0,len(x)):
    if x[i] not in d:
        d.append(x[i])
    elif x[i] in d:
        print(x[i])
        c+=1
        break
if c==0:
    print("unique")
