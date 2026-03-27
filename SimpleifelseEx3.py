#program for accepting a value and decide
# whether it is +ve or -ve or zero -
#simpleifelseEx3.py
value=input("Enter the value: ")
if (value.lstrip("-")) and (value[1:].isdigit()) :
    if int(value)<0:
        print("{} is -ve".format(value))
    if int(value)==0:
        print("{} is zero".format(value))
    if int(value) > 0:
        print("{} is +ve".format(value))

if (not value.isdigit()) and (not value.startswith("-")):
    print("Don't enter string,alnums and symbols")





