#Program for swapping the two integer values using Multi line assignment operator
#ArithmeticExpExp6.py-->Only Integer values
a,b=int(input("Enter the value of a:")),int(input("Enter the value of b:"))
print("*"*50)
print("\toriginal value of a={}".format(a))
print("\toriginal value of b={}".format(b))
print("*"*50)
#logic-4
a=a^b
b=a^b
a=a^b
print("*"*50)
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("*"*50)
