import os 

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||",1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")
            
def display_tasks(tasks):
    if not tasks:
        print(f"No tasks found")
    else:
       for i, task in enumerate(tasks, 1):
           checkbox = "*" if task["done"] else " "
           print(f"{i}, [{checkbox}] {task ['text']}")
           
    print()
    
def task_manager():
    tasks = load_tasks()
    
    while True:
        print("\n ---------- Task List Manager----------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("choose an optiom (1-5)").strip()
        
        match choice:
            case "1":
                text= input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)
                else:
                    print("TASK cannot be empty")
                    
            case "2":
                display_tasks(tasks) 
                
            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number"))      
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(task)
                        print("task marked as done")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter the no")
            
            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete"))      
                    if 1 <= num <= len(tasks):
                        remove = tasks.pop(num-1)
                        save_tasks(task)
                        print(f"task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter the no")
                    
            case "5":
                print("Existing task manager")
                break
            case _:
                print("Please chosse valid no")
        
task_manager()      
        