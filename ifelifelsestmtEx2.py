#program to accept a numerical value and check
# whether it is +ve or -ve or zero
#ifelifelsestmtex2.py
val=float(input("Enter the value:"))
if val==0:
    print("{} is zero".format(val))
elif val<0:
    print("{} is a -ve number".format(val))
else:
    print("{} is a +ve number".format(val))
print("I am from out of else statement")