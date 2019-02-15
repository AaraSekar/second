n1=int(input())
sum1=0
t1=n1
while t1>0:
	digit=t1%10
	sum1=sum1+(digit**3)
	t1=t1//10
if n1==sum1:
	print("yes")
else:
	print("no")
