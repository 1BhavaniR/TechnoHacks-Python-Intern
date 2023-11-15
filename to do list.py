task_list = []

def main(task_list):
    print("""        To-do List\n
        1.Add a task
        2.Delete a task
        2.View task list
        4.Exit
    """)

    choice = int(input("Choose an option from above:"))

    # Adding a Task
    if choice == 1:
        task = str(input("Enter a task :"))
        task_list.append(task)
        print(f"{task} is added in To-do list")

    #Deleting a task
    elif choice == 2:
        task = str(input("Enter a task :"))
        if task in task_list:
            task_list.remove(task)
            print(f"{task} was deleted from list ")
        else:
            print(f"{task} was not found!!!")

    # View to-do list
    elif choice == 3:
        i = 1
        print("Tasks in To-do list")
        if task_list == " ":
            print("There is no tasks in your list!!!")
        else:
            for task in task_list:
                print(f"{i}. {task}")
                i += 1

    # exit
    elif choice == 4:
        exit()

    n = str(input("Do you want to continue(y/n) : "))
    if n == 'y' or n == 'Y':
        main(task_list)
    else:
        exit()

main(task_list)


