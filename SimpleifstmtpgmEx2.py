#program for accepting a value and deciding
# whether the given value is +ve or -ve
#simpleifstmtpgmEx2.py
val=float(input("Enter the value:"))
if(val==0):
    print("{} is zero".format(val))
if(val<0):
    print("{} is -ve".format(val))
if(val>0):
    print("{} is +ve".format(val))