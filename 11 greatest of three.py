a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a == b and b == c and a == c:
    print("All three numbers are equal.")
else:
    result = max(a,b,c)
    print(str(result) + " is greater")


if a >= b and a >= c:
    print(str(a) + " is greater")
elif b >= c and b >= a:
    print(str(b) + " is greater")
elif c > a and c > b:
    print(str(c) + " is greater")
else:
    print("All three numbers are equal")