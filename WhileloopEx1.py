#Program for generating 1 to N numbers where N is positive
#WhileloopEx1.py
n=int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("{} is an Invalid input".format(n))
else:
    print("*" * 40)
    print("\tNumbers within {}".format(n))
    print("*" * 40)
    i=1#Initialization part
    while(i<=n):#Conditional part
        print("\t{}".format(i))
        i=i+1#updating part
    else:
        print("*"*40)
