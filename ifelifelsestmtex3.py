#program for accepting a digit and displaying its name
#ifelifelseex3.py
d=int(input("Enter any digit : "))
if d==0:
    print("zero")
elif d==1:
    print("one")
elif d==2:
    print("two")
elif d==3:
    print("three")
elif d==4:
    print("four")
elif d==5:
    print("five")
elif d==6:
    print("six")
elif d==7:
    print("seven")
elif d==8:
    print("eight")
elif d==9:
    print("nine")
elif d>9:
    print("{} is a number".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is a negative digit".format(d))
elif d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is negative number".format(d))

