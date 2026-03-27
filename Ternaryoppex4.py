#Program for deciding whether the given number is postive or negative or zero
#Ternaryoppex4.py
val=float(input("Enter the value:"))
res="+ve" if val>0 else "-ve" if val<0 else "zero"
print("{} is a {}".format(val,res))