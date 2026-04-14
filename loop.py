evens = 0
odds = 0

table = int(input(" table number : "))
for i in range(2,table+1):
		for j in range(1,11):

			if i % 2 ==0:
				evens +=1

			else:
				odds +=1
			print(j,"X ",i,j*i)
		print()


print(" Total Evens are =",evens)
print("Total odds are  = ",odds)	