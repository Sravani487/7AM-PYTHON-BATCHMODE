#Program for calculation simple interest for the given amount
#ArthimeticExpEx2.py
p=float(input("Enter the principle amount:"))
t=float(input("Enter the time:"))
r=float(input("Enter the rate of interest:"))
si=(p*t*r)/100
totamt=p+si
print("*"*50)
print("\t\tSimple Interest Results")
print("*"*50)
print("\t\tPrinciple amount={}".format(p))
print("\t\ttime:{}".format(t))
print("\t\trate of interest={}".format(r))
print("\t\tSimple interest={}".format(si))
print("\t\ttotal amount to be paid={}".format(totamt))
print("*"*50)
