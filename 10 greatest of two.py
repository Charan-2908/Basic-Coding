a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if a == b:
    print("Both are equal..!")
elif a>b:
    print("a is greater")
else:
    print("b is greater")


if a == b:
    print("Both are equal")
else:
    result = max(a,b)
    print(str(result) + " is greater.")