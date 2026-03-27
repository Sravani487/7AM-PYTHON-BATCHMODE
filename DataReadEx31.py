#Program for reading values dynamically from keyboard and converting using tyoe casting functions.
#DataReadEx31.py
a=input("Enter the value of a =")
b=input("Enter the value of b=")
#Convert the str value into float
x=float(a)
y=float(b)
#multiply them
m=x*y
#Print the values
print("---------------------------------------")
print("First value = {}".format(x))
print("Second value = {}".format(y))
print("Mul of {} ,{} is {}".format(x,y,m))
print("---------------------------------------")