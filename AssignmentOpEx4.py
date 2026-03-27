#Program for swapping the numbers using multi line assignment operator
#AssignmentOpEx4.py
a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
print("*"*50)
print("\toriginal value of a:{}".format(a))
print("\toriginal value of b:{}".format(b))
print("*"*50)
a=a+b
b=a-b
a=a-b
print("*"*50)
print("\tSwapped value of a:{}".format(a))
print("\tSwapped value of b:{}".format(b))
print("*"*50)