n=int(input())
sum=0
while n>0:
	r=n%10
	sum=sum+r
	n=n//10
sum=str(sum)
if sum==sum[::-1]:
	print("YES")
else:
	print("NO")
