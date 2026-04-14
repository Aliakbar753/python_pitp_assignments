name = input("Enter your name : ")
age = int(input("Enter your age : "))
ent_exam_score = int(input("Enter your enterence Marks : "))
family_income = float(input("Enter your annual family income : "))

# step 1. checking age and score 
if age < 16 :
	print(f"Sorry {name}!, you are too Young")

elif ent_exam_score < 60 :
	print(f"Sorry {name}!, your score is too low")

# Step 2. checking family annual income 

if age >= 16 and ent_exam_score >= 60 :
	if family_income < 30000:
		print(f"congrates {name}!, your are admitted with full scholarship")

	elif family_income < 79999 :
		print(f"congrates {name}!, you are admitted with partial scholarship")

	else:
		print(f"{name}, you are admitted without scholarship")
		








