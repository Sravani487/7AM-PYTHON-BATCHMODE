#program for displaying the biggest of given two numbers
#Ternaryoppex2.py
a=float(input("Enter first value:"))
b=float(input("Enter second value:"))
bv=a if a>b else b if b>a else "both are equal"
print("big({},{}) = {}".format(a,b,bv))