#program for calculating product of N natural numbers and where n is +ve.
#WhileloopEx7.py
n=int(input("Enter how many numbers you want to generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("\tNatural numbers within {}".format(n))
    print("*"*40)
    i=1
    p=1#multiplicative identity
    while(i<=n):
        print("\t\t\t{}".format(i))
        p=p*i
        i+=1
    else:
        print("*"*40)
        print("\tproduct={}".format(p))
        print("*" * 40)

