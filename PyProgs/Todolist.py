#A TO-DO LIST APPLICATION

print("Welcome to the TO-DO LIST Application")

tasks = []


while True:
    
    print("OPTIONS")
    print("1. Add Task")
    print("2. Display Task")
    print("3. Remove Task")
    print("4. Exit")

    
    choice = input("What would you like to do?: ")
    
    if choice == "1":
        print("Enter your task")
        task = input("Add task: ")
        tasks.append(task)
    
    elif choice == "2":
        print("Displaying Tasks: ")
        for task in tasks:
            print(task)
    
    elif choice == "3":
        rem_task = input("Enter the task you want to remove?: ")
        tasks.remove(rem_task)
    
    elif choice == "4":
        print("Quitting.....")
        break
    
    else:
        print("Invalid Option....")


