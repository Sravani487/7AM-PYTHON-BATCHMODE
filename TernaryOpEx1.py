#program for demonstrating Palindrome using Ternary operator
#TernaryopEx1.py
val=input("Enter the string :")
res="Palindrome" if (val==val[::-1]) else "Not Palindrome"
print("{} is {}".format(val,res))
