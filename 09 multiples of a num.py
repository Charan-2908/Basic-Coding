n = int(input("Which number multiples do you want: "))

for i in range(1,11):
    print(n, 'X', i, '=', n*i)


i = 1
while i < n+1:
    print(n, 'X', i, '=', n*i)
    i += 1