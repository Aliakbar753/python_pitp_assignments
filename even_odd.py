evens = []
odds = []

for i in range(20):
    if i % 2 == 0:
        evens.append(i)

    else:
        odds.append(i)    

        
print(f"Evens are = {evens}")
print(f"Odds are = {odds}")

if evens != [] and odds != []:
    print(f"Maximum in Even = {max(evens)}")
    print(f"Minimum in Evens = {min(evens)}")
    print(f" Sum of Evens = {sum(evens)}")
    print(f"Averge of Evens = { sum(evens)/len(evens)}")


    print(f"Maximum in odds = {max(odds)}")
    print(f"Minimum in odds = {min(odds)}")
    print(f" Sum of odds = {sum(odds)}")
    print(f"Average of odds = {sum(odds)/len(odds)}")

else:
    print("Evens or Odds list is empty")