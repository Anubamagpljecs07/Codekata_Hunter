s=input()
r=input()
a=len(r)
for i in range(0,len(s)):
	b=s[i:i+a]
	if b==r:
		print(i)
		break
