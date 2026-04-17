data = [1,2,3,4,5,6]
print(data)

print(f"Maximum number is : {max(data)}")
print(f"Minimum number is : {min(data)}")

print(f"sum of all number is : {sum(data)}")

for i in data:
 if i%2==0:
  print(f"{i} is an Even number")
 else:
  print(f"{i} is an Odd number")
 