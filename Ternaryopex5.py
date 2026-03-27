#program for accepting a numerical value and check whether it is even or odd
#Ternaryopex5.py
val=int(input("Enter any integer value:"))
res="Invalid input" if val<=0 else "Even" if val%2==0 else "odd"
print("{} is {}".format(val,res))