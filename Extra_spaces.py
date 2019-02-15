import re
s=input()
x=re.sub('\s+', ' ', s).strip()
print(x)
