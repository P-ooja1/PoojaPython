# Linear Search

x = int(input("Enter the range "))
y = []
for j in range(0, x, 1):
    b = input("Enter the list value")
    y.append(b)
print(y)
z = input("Enter the search list value")
for k in range(0, len(y),1) :
    if z == y[k] :
        print(k)