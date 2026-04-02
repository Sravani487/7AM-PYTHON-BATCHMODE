#program for displaying numbers 1 to N where N is +ve
#ForloopEx2.py
n=int(input("Enter how many numbers you want to generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    i=1
    print("Numbers within {}".format(n))
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-----------------")