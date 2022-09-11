a = int(input("Enter num1"))
b = int(input("Enter num2"))
print(a // b) #Floor division converts deci value to whole int value
print(a / b)

#Chnage Varialble Name and simplify code
Number = int(input("Enter value"))
if Number % 2 != 0:
    print("Odd")
elif Number % 2 == 0 and Number >= 2 and Number <= 5:
    print("Not weird")
elif Number % 2 == 0 and Number >= 6 and Number <= 20:
    print("weird")
elif Number % 2 == 0 and Number >= 20:
    print("Not weird")
else:
    print("Null value")