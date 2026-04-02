#Program for displaying numbers and sum of its squares and cubes for
# the given natural number where N is +ve.
#ForloopEx6.py
n=int(input("Enter how many numbers you want to generate:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("*"*40)
    print("Numbers\t\t\tsquares\t\t\tcubes")
    print("*" * 40)
    i=1
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t{}\t\t\t\t{}\t\t\t\t{}".format(i, i ** 2, i ** 3))
        s=s+i
        ss=ss+i*i
        cs=cs+i**3
        i=i+1
    else:
        print("*"*40)
        print("\tsum={}\t\t\t{}\t\t\t{}".format(s,ss,cs))
        print("*" * 40)
