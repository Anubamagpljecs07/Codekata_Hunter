#ganu
n=int(input())
l=[int(i) for i in input().split()]
y=[]
for i in range(len(l)):
    for j in range(len(l)):
        if i<j :
            if (l[i]+l[j])==0:  
                y.append(l[i])
                y.append(l[j])
                i=i+1
            elif (l[i]+l[j])==-1:
                y.append(l[i])
                y.append(l[j])
                i=i+1
            elif (l[i]+l[j])==1:
                y.append(l[i])  
                y.append(l[j])
                i=i+1
for h in range(0,2):
    if h==0:
        print(y[h],end="")
    else:
        print("",y[h],end="")
