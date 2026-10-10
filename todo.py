tasks=[]
while True:
    print("\n---TO-DO LIST---")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Update Task")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        task=input("Enter your task:")
        tasks.append(task)
        print("Task added sucessfully!")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i,task in enumerate(tasks,1):
             print(i,".",task)
    elif choice=="3":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\nYour tasks:")
            for i,task in enumerate(tasks,1):
                print(i,".",task)
                number=int(input("Enter task number to delete:"))
        if 1<=number<=len(tasks):
            tasks.pop(number-1)
            print("task deleted successfully!")
        else:
            print("Invalid task number.")
    elif choice=="4":
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i,task in enumerate(tasks,1):
                print(i,".",task)
                number=int(input("Enter task number to update:"))
                if 1<=number<=len(tasks):
                    new_task=input("Enter the new task:")
                    tasks[number-1]=new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
    elif choice=="5":
                print("Thank you for using the To-Do List!")
                break
    else:
            print("invalid choice.Please try again.")