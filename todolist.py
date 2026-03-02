# load task
import json

tasks = []
# load task from file
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    pass


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("task added")


add_task()


def view_task():
    if not tasks:
        print("No task")
    else:
        print("Task:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


view_task()


def delete_task():
    view_task()
    try:
        task_num = int(input("Enter a task number to delete:"))print
        del tasks[task_num - 1]
        print("task deleted!")
    except (ValueError, IndexError):
        print("Invalid task number!")


def main():
    while True:
        print("\nTo-Domlist App")
        print("1.Add task")
        print("2.view task")
        print("delete task")
        print("4.Quit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            save_task()
            break
        else:
            print("Invalid choice!")
            if __name__ == "__main__":
                main()


def save_task():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved to tasks.json")
