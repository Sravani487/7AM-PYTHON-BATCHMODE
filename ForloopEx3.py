#program for displaying all even numbers within N where N is +ve.
#ForloopEx3.py
n=int(input("Enter how many even numbers need to generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("for loop--Even numbers within {}".format(n))
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
        print("*" * 40)
        print("for loop--Odd numbers within {}".format(n))
        for i in range(1,n+1,2):
            print("\t{}".format(i))
        else:
            print("*"*50)