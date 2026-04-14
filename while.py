table = int(input("enter the table: "))
total = 0
evens = 0
odds = 0

i = 1 
while i<=table:
	for j in range(3,11):
		print(j, "X = ",j*i)
		total += j*i
		if j%2==0:
			evens +=1

		else:
			odds +=1


	print("Addition of numbers = ",total )
	print( " Total Evens = ", evens)
	print(" Total odds  = ",odds)
	print()
	total = 0

	i +=1	