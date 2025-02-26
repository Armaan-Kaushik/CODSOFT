import json

class SimpleToDo:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.task_list = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.task_list, file, indent=4)

    def add_task(self, new_task):
        self.task_list.append({"task": new_task, "done": False})
        self.save_tasks()
        print("Task added!")

    def show_tasks(self):
        if not self.task_list:
            print("No tasks yet!")
        for i, item in enumerate(self.task_list, 1):
            mark = "[X]" if item["done"] else "[ ]"
            print(f"{i}. {mark} {item['task']}")

    def complete_task(self, task_no):
        if 1 <= task_no <= len(self.task_list):
            self.task_list[task_no - 1]["done"] = True
            self.save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid number!")

    def remove_task(self, task_no):
        if 1 <= task_no <= len(self.task_list):
            del self.task_list[task_no - 1]
            self.save_tasks()
            print("Task removed!")
        else:
            print("Invalid number!")

if __name__ == "__main__":
    todo = SimpleToDo()
    while True:
        print("\nSimple To-Do List")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            try:
                num = int(input("Enter task number to complete: "))
                todo.complete_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            todo.show_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                todo.remove_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")
