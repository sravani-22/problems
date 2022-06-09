a=input("enter the string")
b=input("enter the string to check")
a=a.lower()
b=b.lower()
a=[ i for in a.split()]
b=[i for in b.split()]
a.sort()
b.sort()
if(a==b):
	print("enter string in anagram")
else:
	print("not an anagram")
