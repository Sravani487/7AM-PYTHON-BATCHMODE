#Program for swapping the two integer values using Multi line assignment operator
#ArithmeticExpExp4.py-->Only Integer values
a,b=int(input("Enter the value of a:")),int(input("Enter the value of b:"))
print("*"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
#logic-3
a=a+b
b=a-b
a=a-b
print("*"*50)
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("*"*50)