# def students():
#     print("this is a function named students")

# students()

# def data():
#     n = int(input("enter to"))
#     for i in range(1,n+1):
#         print(i)


# data()   

# def loop(num):
#     for i in range(1,num+1):
#         print(i)

# num = int(input("Enter a number : "))
# loop(num)

def add(num1,num2):
    print(f"Addition =  {num1+num2}")

def sub(num1,num2):
    print(f"Subtraction = {num1-num2}")

def muultiple(num1,num2):
    print(f"Multiplication = {num1*num2}")

def divison(num1, num2):
    print(f"Divison = {num1/num2}")

while True:

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    choice = input("what to do  + - * / (if wnat to exit = stop)")

    if choice != '+' or choice != '-' or choice != '*' or choice != '/' or choice != 'stop':
        print('please Enter valid choice')
    else:

        if choice=='+':
            add(num1,num2)

        elif choice == '-':
            sub(num1,num2)

        elif choice == '*':
            muultiple(num1,num2)

        elif choice == '/':
            if num1>0 and num2>0:
                divison(num1,num2)

            else:   
                print("can not divide by 0")

        elif choice == 'stop':
            break