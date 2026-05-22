tasks = []

while True:
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")

    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to remove: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number!")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        print("Exiting To-Do App...")
        break

    else:
        print("Invalid choice!")
