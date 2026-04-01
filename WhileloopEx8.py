#program for cal factorial of a number
#n!=1x2x3x....n or nx(n-1)x(n-2)....x0!
#WhileloopEx8.py
n=int(input("Enter the number for cal factorial:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i+=1
    else:
        print("Factorial of {} is {}".format(n,fact))
