#Program for accepting a value and checking
# whether it is a palindrome or not by using simple if statement.
#SimpleifstmtEx1.py
val=input("Enter any value :")
if (val==val[::-1]):
    print("{} is palindrome".format(val))
if(val!=val[::-1]):
    print("{} is not palindrome".format(val))
print("Program execution is completed")
