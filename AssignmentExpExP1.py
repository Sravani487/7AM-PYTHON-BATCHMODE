#Program to calculate all arithmetic operations by using multi line assignment operator.
#ArithmeticExpExP1.py
a,b=float(input("Enter the value of a : ")),float(input("Enter the value of b :"))
add,sub,mul,div,floordiv,moddiv,pow = a+b,a-b,a*b,a/b,a//b,a%b,a**b
print("*"*50)
print("Arithmetic Operators with multi line assignment op")
print("*"*50)
print("\t\tsum({},{})={}".format(a,b,add))
print(f"\t\tsub({a},{b})={sub}")
print(f"\t\tmul({a},{b})={mul}")
print(f"\t\tdiv({a},{b})={div}")
print(f"\t\tfloordiv({a},{b})={floordiv}")
print(f"\t\tmoddiv({a},{b})={moddiv}")
print(f"\t\tpow({a},{b})={pow}")
print("*"*50)
