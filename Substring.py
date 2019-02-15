s=input()
r=input()
a=len(r)
ac=0
for i in range(0,len(s)):
	b=s[i:i+a]
	if b==r:
		ac=ac+1
		b=i
		break
if ac==0:
	print("-1")
else:
	print(b)
