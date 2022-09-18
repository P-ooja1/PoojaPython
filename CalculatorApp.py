# 1.get three string inputs
# 2.first two inputs to be converted to integer  and third input is string with symbols
# 3.add , sub, mul, division and remainder division
# 4.change the negative value as positive

a = str(input("Enter the value"))
b = str(input("Enter the value"))
c = str(input("Enter the math function"))
if c == '+':
    res: int = int(a)+int(b)
    print(res)
    if res < 0:
        d = res*(-1)
        print(d)
    else:
        print("Null value")
elif c == '-':
    res = int(a)-int(b)
    print(res)
    if res < 0:
        d = res * (-1)
        print(d)
    else:
        print("Null value")
elif c == '*':
    res = int(a)*int(b)
    print(res)
    if res < 0:
        d = res * (-1)
        print(d)
    else:
        print("Null value")
elif c == '/':
    res = int(a)/int(b)
    print(res)
    if res < 0:
        d = res * (-1)
        print(d)
    else:
        print("Null value")
elif c == '%':
    res = int(a)%int(b)
    print(res)
    if res < 0:
        d = res * (-1)
        print(d)
    else:
        print("Null value")
else:
    print("Invalid value")