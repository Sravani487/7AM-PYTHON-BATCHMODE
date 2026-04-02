#Program for generating mul table for a given number where N is +ve
#ForloopEx9.py
n=int(input("Enter a number for generating multiplication table:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    print("-"*40)
    print("\tfor loop--Mul Table for {}".format(n))
    for i in range(1,11):
        print("\t{} * {} = {}".format(n,i,n*i))
    else:
        print("-"*40)
    print("-"*40)
    print("\twhile loop--Mul table for {}".format(n))
    i=1
    while(i<=10):
        print("\t{} * {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("-"*40)


