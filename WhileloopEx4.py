#Program for calculating sum of N natural numbers where N is +ve.
#WhileloopEx4.py
n=int(input("Enter how many natural numbers sum you want to find: "))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("Natural Numbers within {}".format(n))
    print("*"*40)
    i=1#Initialization part
    s=0#Initialization part of Additive identity
    while(i<=n):
        print("\t{}".format(i))
        s=s+i#Accumulating i values
        i+=1
    else:
        print("*"*40)
        print("sum={}".format(s))
        print("*" * 40)