import json


def menu():
    todos = load_todo()

    while True:
        show_menu()
        choice = input("Enter the the Operation you want to do: ")
        print("Id", "-", "Items", "-", "Status")
        _id = todos[-1]["id"] + 1 if len(todos) > 0 else 1

        if choice == "1":
            for l in todos:
                print(l["id"], "-", l["task"], "-", l["completed"])

            if not close():
                break

        elif choice == "2":
            save_todos(todos)
            is_continue = close()
            if not is_continue:
                break

        elif choice == "3":
            item = input("Enter the Item you want to add to the todo list: ")
            completed = input("Is the task completed y/n: ")
            is_completed = True if completed == "y" else False
            todos.append({"id": _id, "task": item, "completed": is_completed})
            is_continue = close()
            if not is_continue:
                break

        elif choice == "4":
            item_id = input("Enter the Item Id: ")
            is_item_present = any(todo["id"] == item_id for todo in todos)
            if not is_item_present:
                print("There is no such item in the list")
            else:
                print("-------- Edit Menu---------")
                print("1. Edit Item")
                print("2. Edit Status")
                print("3. Cancel Edit Menu")
                print("---------------------------")
                edit_option = input("Enter the Number from the above Edit Menu to Edit: ")

                if edit_option == "1":
                    edited_item = input("Enter the Item: ")
                    todos[item_id].item = edited_item
                    is_continue = close()
                    if not is_continue:
                        break
                elif edit_option == "2":
                    edited_item_status = input("Do you want to make status True or False, Select 'y' for True and 'n' for False y/n: ")
                    todos[item_id].completed = edited_item_status == "y"
                    is_continue = close()
                    if not is_continue:
                        break
                   
        elif choice == "5":
            item_id = input("Enter the Item Id to Delete: ")
            is_item_present = any(todo["id"] != item_id for todo in todos)
            if not is_item_present:
                print("There is no such item in the list")
            else:
                confirm_once = input("Are your sure you want to delete the Item from the list y/n: ")
                if confirm_once == "y":
                    filter_todo = filter(lambda item: item["id"] != item_id, todos)
                    todos = list(filter_todo)
                    save_todos(todos)
                    is_continue = close()
                    if not is_continue:
                        break
        else:
            break


def close():
    check = input("Do you want to continue y/n, ")
    return check == "y"


# Menu List
def show_menu():
    print("------ Todo Menu ------")
    print("1. Load Task")
    print("2. Save Task")
    print("3. Add Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("-----------------------------")


# Load Todos
def load_todo():
    with open("todo.json", "r") as file:
        return json.load(file)


# Save Todo
def save_todos(list):
    with open("todo.json", "w") as file:
        json.dump(list, file, indent=4)


if __name__ == "__main__":
    menu()
