#Program for swapping the numbers using multi line assignment operator
#AssignmentOpEx3.py
a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
print("*"*50)
print("\toriginal value of a:{}".format(a))
print("\toriginal value of b:{}".format(b))
print("*"*50)
x=a
a=b
b=x
print("*"*50)
print("\tSwapped value of a:{}".format(a))
print("\tSwapped value of b:{}".format(b))
print("*"*50)