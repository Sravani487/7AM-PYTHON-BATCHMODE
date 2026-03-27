#program to check whether the entered value is palindrome or not
#simpleifstmtpgmex1.py
val=input("Enter the value:")
if (val==val[::-1]):
    print("{} is palindrome".format(val))
if (val!=val[::-1]):
    print("{} is not palindrome".format(val))
print("Program execution completed")
