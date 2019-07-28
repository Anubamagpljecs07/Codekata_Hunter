class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        if self.items==[]:
            return True
        else:
            return False
    def get(self):
        return self.items
a=input()
s=Stack()
is_pal=False
if len(a)%2==0:
    pass
else:
    a=a[0:len(a)//2]+a[(len(a)//2)+1:len(a)]
for i in range(len(a)//2):
    g=a[i]
    s.push(g)
for i in range((len(a)//2),len(a)):
    g=a[i]
    top=s.pop()
    if top==g :
        is_pal=True
    else:
        is_pal=False
        break
    
if s.is_empty() and is_pal:
    print("yes")
else:
    print("No")

