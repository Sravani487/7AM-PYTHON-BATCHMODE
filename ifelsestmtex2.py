#program for checking whether the given number is +ve,-ve or zero
#ifelsestmtex2.py
val=float(input("Enter the value:"))
if val==0:
    print("{} is zero".format(val))
else:
    if val<0:
        print("{} is a -ve value".format(val))
    else:
        print("{} is a +ve value".format(val))
    print("this executed from inner if-else statement")
print("this executed from outer if-else statement")