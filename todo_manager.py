# todo_manager.py 

# 1. Start with a pre-populated list of 3 tasks
to_do = ["Buy groceries", "Finish homework", "Call the dentist"]

# Display the current to-do list (numbered, starting from 1)
print("========================================")
print("         My To-Do List")
print("========================================")
print("1.", to_do[0])
print("2.", to_do[1])
print("3.", to_do[2])
print("\nTotal tasks:", len(to_do))
print("========================================")

# عرض الخيارات للمستخدم
print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task")



#Let the user add a new task (append)
new_task = input("\nChoice: 1 -> Enter new task: ")
to_do.append(new_task)

print("\nUpdated list (After Append):")
print("1.", to_do[0])
print("2.", to_do[1])
print("3.", to_do[2])
print("4.", to_do[3])
print("\nTotal tasks:", len(to_do))
print("========================================")

# Let the user remove a task by number (pop)
task_num = input("\nChoice: 2 -> Enter the number of the task to remove: ")


try:
    index_to_remove = int(task_num) - 1
    removed_task = to_do.pop(index_to_remove)
    print(f"\nSuccessfully removed: '{removed_task}'")
except (ValueError, IndexError):
    print("\nError: Invalid task number!")

# Display the updated list after each operation
print("\nUpdated list (Final):")
print("1.", to_do[0])
print("2.", to_do[1])
print("3.", to_do[2])

#Show the total number of tasks remaining
print("\nTotal tasks:", len(to_do))
print("========================================")