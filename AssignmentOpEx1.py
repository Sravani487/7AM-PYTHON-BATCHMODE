#Program for calculating assignment operators by using multi line assignment op
#AssignmentOpEx1.py
a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
add,sub,mul,div,floordiv,moddiv,exp=a+b,a-b,a*b,a/b,a//b,a%b,a**b
print("*"*40)
print("\t\tAssignment Operators")
print("*"*40)
print(f"\t\tsum({a},{b})={a+b}")
print(f"\t\tsub({a},{b})={a-b}")
print(f"\t\tmul({a},{b})={a*b}")
print(f"\t\tdiv({a},{b})={a/b}")
print(f"\t\tfloordiv({a},{b})={a//b}")
print(f"\t\tmoddiv({a},{b})={a%b}")
print(f"\t\texp({a},{b})={a**b}")
print("*"*40)
