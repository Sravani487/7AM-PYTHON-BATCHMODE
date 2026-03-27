#program for accepting a string and checking whether it is a palindrome or not
#simpleifelifex1.py
val=input("Enter the value:")
if val==val[::-1]:
    print("{} is palindrome".format(val))
elif val!=val[::-1]:
    print("{} is not a palindrome".format(val))
print("Program execution completed")