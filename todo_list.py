def menu():
    print('TODO LIST APP')
    print(f"1. view tasks")
    print(f"2. Add task")
    print(f"3. delete task")
    print(f"4. exit")

def viewtasks(tasks):
    if tasks == []:
        print('Not Any Task')
    else:
        print("\n tasks")
        index =1
        for i in tasks:
            print(f"{index}. {i}")
            index +=1
    print("====="*10)

def addtask(tasks):
    task = input("Enter task to add : ")
    tasks.append(task)
    print("task added succesfully")
    print("====="*10)

def deletetask(tasks):
    if tasks == []:
        print('not any task is availble')
    else:
        viewtasks(tasks)
        task_del = int(input("Enter task number to delete : "))
        task = tasks.pop(task_del-1)
        print(f"{task} is deleted")
        print("====="*10)
    

def todo():
    tasks=[]
    while True:
        menu()
        choice = input("Enter option 1-4 : ")

        if choice == '1':
            viewtasks(tasks)
        elif choice == '2':
            addtask(tasks)

        elif choice == '3':
            deletetask(tasks)
        
        elif choice == '4':
            print("Program exited.")
            break
        else: 
            print('invalid choice , try again')

todo()