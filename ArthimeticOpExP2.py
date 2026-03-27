#Program to display simple interest and total amount calculation.
#ArthimeticOpExp2.py
p=float(input("Enter Principle amount :"))
t=float(input("Enter time :"))
r=float(input("Enter the rate of interest :"))
si=(p*t*r)/100
totamt=p+si
print("--------------------------------------")
print("\t\tPrinciple amount = {}".format(p))
print("\t\ttime ={}".format(t))
print("\t\tRate of interest = {}".format(r))
print("\t\tsimple interest = {}".format(si))
print("\t\tTotal Amount to pay= {}".format(totamt))
print("--------------------------------------")