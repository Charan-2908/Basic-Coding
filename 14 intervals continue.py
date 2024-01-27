low = int(input("Enter a number: "))
high = int(input("Enter another number: "))

for i in range(low, high+1):
    if i % 5 == 0:
        continue
    print(i, end=" ")

while low <= high:
    if low % 5 == 0:
        low += 1
        continue
    print(low, end=",")
    low += 1
