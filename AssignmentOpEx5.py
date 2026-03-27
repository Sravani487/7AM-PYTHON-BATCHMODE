#Program for swapping the numbers using multi line assignment operator
#AssignmentOpEx5.py
a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:")) #a=10,b=3
print("*"*50)
print("\toriginal value of a:{}".format(a))
print("\toriginal value of b:{}".format(b))
print("*"*50)
a=a*b  #a=30
b=a//b #b=30//3 => b=10
a=a//b  #a=30//10 => a=3
print("*"*50)
print("\tSwapped value of a:{}".format(a))
print("\tSwapped value of b:{}".format(b))
print("*"*50)