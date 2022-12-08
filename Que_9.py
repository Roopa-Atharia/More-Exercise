n=int(input("enter the num"))
x=n
sum=0
while x>0:
	r=x%10
	sum=sum+r
	x=x//10
if n%sum==0:
	print(n,"harshad")
else:
	print("not")



a=int(input("enter : "))
i=1
while i<=a:
	b=str(i)
	j=0
	sum=0
	while j<len(b):
		sum+=int(b[j])
		j+=1
	if i%sum==0:
		print(i)
	i+=1










