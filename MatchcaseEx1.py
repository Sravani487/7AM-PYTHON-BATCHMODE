#Program for performing all arthimetic operations by using match case statement
#MatchcaseEx1.py
print("*"*50)
print("\t\tArithmetic Operations")
print("*"*50)
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("*"*50)
ch=int(input("Enter your choice:"))
match(ch):
    case 1:
        a,b=float(input("Enter the first value:")),float(input("Enter the second value:"))
        print("\tsum({},{})={}".format(a,b,a+b))
    case 2:
        a,b = float(input("Enter the first value:")),float(input("Enter the second value:"))
        print("\tsub({},{})={}".format(a,b,a-b))
    case 3:
        a,b = float(input("Enter the first value:")),float(input("Enter the second value:"))
        print("\tmul({},{})={}".format(a,b,a*b))
    case 4:
        a,b = float(input("Enter the first value:")), float(input("Enter the second value:"))
        print("\tdiv=({},{})={}".format(a,b,a/b))
        print("\tfloordiv({},{})={}".format(a,b,a//b))
    case 5:
        a,b = float(input("Enter the first value:")), float(input("Enter the second value:"))
        print("\tmodulo division({},{})={}".format(a,b,a%b))
    case 6:
        a,b = float(input("Enter the base value:")), float(input("Enter the power value:"))
        print("\tpow({},{})={}".format(a,b,a**b))
    case 7:
        print("Thanks for using the program")
    case _:
        print("your selection of operation is wrong")
print("The program execution for match case is completed")








