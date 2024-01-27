low = int(input("Enter a number: "))
high = int(input("Enter another number: "))

for i in range(low,high+1):
    print(i, end=" ")
    if i % 13 == 0:
        break

while low < high:
    print(low, end=" ")
    if low % 13 == 0:
        break
    low += 1
