#program for displaying all even numbers in descending order within N where N is +ve.
#ForloopEx4.py
n=int(input("Enter how many even numbers need to generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("for loop--Even numbers within {}".format(n))
    if(n%2!=0):
        n=n-1
    for i in range(n,1,-2):
        print("\t{}".format(i))