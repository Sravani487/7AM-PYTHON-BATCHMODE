#program for finding factors of a number
#WhileloopEx10.py
n=int(input("Enter the number to find the factors:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*50)
    print("\t factors of {}".format(n))
    print("*" * 50)
    i=1
    while(i<=n//2):
        if n%i==0:
            print("\t\t{}".format(i))
        i=i+1
    else:
        print("\t\t{}".format(n))
        print("*"*50)