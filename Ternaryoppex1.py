#program for deciding whether the entered String is palindrome or not
#Ternaryoppex1.py
val=input("Enter the value:")
res="palindrome" if val==val[::-1] else "Not Palindrome"
print("{} is {}".format(val,res))
