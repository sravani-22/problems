def fact(n):
	if n==1:
		return 1
	else
		return n*fact(n-1)
num =int(input("enter the number"))
if num<0;
	print(" factorial does not exsit for negative numbers")
elif num==0:
	print("the factorial of 0 is 1")
else:
	print("the factorial of ",num,"is ",fact(num))
