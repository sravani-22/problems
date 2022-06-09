(def c (p,r,t):
	if t==0:
		return p
	else:
		return c(p+(p*r)/100,r,t-1)
p=int(input("enter the value of the principle amount"))
t=int(input("enter the time period"))
r=int(input("enter the value of the rate of the intrest"))
print(c(p,r,t))


