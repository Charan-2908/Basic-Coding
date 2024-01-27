age = int(input("Enter your age: "))

if age < 18:
    print("Cannot Vote...!")
else:
    print("Eligible for Voting.....!")
    
result = "Vote" if age >= 18 else "Cannot Vote"
print(result)

print("Vote") if age >= 18 else print("cannot vote")