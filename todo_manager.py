
# todo_manager.py — A simple interactive to-do list manager

# 1. Start with a pre-populated list of 3 tasks
todo_list = ["Buy groceries", "Finish homework", "Call the dentist"]

# Display the initial to-do list (numbered, starting from 1)
print("=" * 40)
print("         My To-Do List")
print("=" * 40)
for i in range(len(todo_list)):
    print(f"{i + 1}. {todo_list[i]}")

print(f"\nTotal tasks: {len(todo_list)}")
print("=" * 40)

# Prompt user for an action
print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task")

choice = input("\nChoice: ")

if choice == "1":
    # 2. Let the user add a new task (append)
    new_task = input("Enter new task: ")
    todo_list.append(new_task)
    
    # Display the updated list after addition
    print("\nUpdated list:")
    for i in range(len(todo_list)):
        print(f"{i + 1}. {todo_list[i]}")
        
    # Show the total number of tasks remaining
    print(f"\nTotal tasks: {len(todo_list)}")

elif choice == "2":
    # 3. Let the user remove a task by number (pop) using try/except for error handling
    try:
        task_num = int(input("Enter the task number to remove: "))
        
        # Convert 1-based user input to 0-based index for Python's pop()
        removed_task = todo_list.pop(task_num - 1)
        print(f"\nRemoved: '{removed_task}'")
        
        # Display the updated list after removal
        print("\nUpdated list:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")
            
        # Show the total number of tasks remaining
        print(f"\nTotal tasks: {len(todo_list)}")
        
    except (ValueError, IndexError):
        # Handle invalid inputs (e.g., text instead of numbers, or out-of-range numbers)
        print("\n[Error] Invalid task number! Please enter a valid number from the list.")

else:
    print("\n[Error] Invalid choice. Please restart the program and select 1 or 2.")
