#Program for calculating sum of squares and cubes of N natural numbers where N is +ve
#WhileloopEx6.py
n=int(input("Enter how many numbers(squares and cubes) you want to generate: "))
if n<=0 :
    print("{} is an invalid input".format(n))
else:
    print("*"*50)
    print("Natural numbers\t\t\tSquares\t\t\tcubes")
    print("*"*50)
    i=1
    s=0#initialization part
    ss=0#initialization part
    cs=0#initialization part
    while(i<=n):
        print("\t{}\t\t\t\t\t{}\t\t\t\t\t{}".format(i,i*i,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i+=1
    else:
        print("*"*50)
        print("sum={}\t\t\t\t\t{}\t\t\t\t\t{}".format(s,ss,cs))
        print("*" * 50)