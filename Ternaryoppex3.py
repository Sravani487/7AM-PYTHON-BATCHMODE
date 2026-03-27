#Program for finding the biggest of three numbers
#Ternaryoppex3.py
a=float(input("Enter the first value:"))
b=float(input("Enter the second value:"))
c=float(input("Enter the third value:"))
bv=a if(a>=b and a>c) else b if(b>=c and b>a) else c if(c>=a and c>b) else "all are equal"
print("big({},{},{}={})".format(a,b,c,bv))