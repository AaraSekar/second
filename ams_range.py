n1,k1=map(int,input().split())
for j in range (n1,k1+1):
     sum1=0
     t1=j
     while t1>0:
	       digit=t1%10
	       sum1=sum1+(digit**3)
	       t1=t1//10
     if j==sum1:
	       print(j,end=" ")
