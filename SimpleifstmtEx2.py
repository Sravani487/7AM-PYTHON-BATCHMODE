#Program for accepting the value and checking
# whether it is positive or negative value using simple if statement
#SimpleifstatEx2.py
value=float(input("Enter any value:"))
if value==0 :
    print("{} is zero".format(value))
if value<=0 :
    print("{} is negative value".format(value))
if value>=0:
    print("{} is positive value".format(value))
print("Program execution is completed.")
