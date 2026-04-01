#Program for generating N to 1 numbers where N is positive.
#Display the numbers in descending order
#WhileloopEx3.py
n=input("Enter how many numbers you want generate in a descending order:")
if n.isalpha():
    print("{} is an invalid input".format(n))
elif not n.isdigit():
    print("{} is an invalid input".format(n))
elif int(n)<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("Numbers within {}".format(n))
    print("*"*40)
    i=int(n)
    while(i>=1):
        print("\t{}".format(i))
        i=i-1
    else:
        print("*"*40)