#program for accepting a digit and displaying its name
#DigitEx2.py
d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
dig=int(input("Enter the number :"))
print("{} is {}".format(dig,d.get(dig) if d.get(dig)!=None
else "+ve number" if dig>9 else "-ve digit"
if dig in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-ve number"))

