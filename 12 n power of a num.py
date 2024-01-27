base = float(input("Enter the base number: "))
expo = float(input("Enter the expo number: "))

result = base ** expo
print(result)

num = 1
i = 1
while i <= expo:
    num *= base
    i += 1
print(num)

# num1 = 1
# for j in range(0,expo):   
#     num1 *= base                 this will not work if expo is float
# print(num1)