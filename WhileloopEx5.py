#Program for calculating sum of squares of N natural numbers where N is +ve
#WhileloopEx5.py
n=int(input("Enter how many numbers you want t generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("Natural numbers\t\t\tSquares")
    print("*"*40)
    i=1
    s=0#Initialization part-->Additive part
    ss=0#Initialization part -->Squares Additive part
    while(i<=n):
        print("\t{}\t\t\t\t\t{}".format(i,i*i))
        s=s+i
        ss=ss+i**2
        i+=1
    else:
        print("*"*40)
        print("sum={}\t\t\t\t\t{}".format(s,ss))
