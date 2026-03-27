#program accepting two numerical values and finding biggest among them and checking for equality
a=float(input("Enter the value of a :"))
b=float(input("Enter the value of b :"))
bv=a if a>b else b if b>a else "Both are equal"
print("Big({},{})={}".format(a,b,bv))
