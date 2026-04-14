secret_num = 7

guess_num = int(input("Enter number to guess"))

if guess_num == secret_num:
	print("wow you guessed it")

elif guess_num > secret_num:
	print("too high")

else:
	print("too low")	