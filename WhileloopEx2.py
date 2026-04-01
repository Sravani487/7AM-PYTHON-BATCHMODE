#Program for generating 1 to N numbers where N is positive.
# We are taking N as string.
#WhileloopEx2.py
n=input("Enter how many numbers you want to generate:")
if n.isalpha():
    print("{} is an invalid number".format(n))
elif not n.isdigit():
    print("{} is an invalid number".format(n))
elif int(n)<=0:
    print("{} is an invalid number".format(n))
else:
    print("*"*40)
    print("Numbers within {}".format(n))
    print("*" * 40)
    i=1
    while(i<=int(n)):
        print("\t{}".format(i))
        i=i+1
    else:
        print("*"*40)


