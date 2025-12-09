import json


def load_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)


def show_menu():
    print("--------- SHOW MENU ---------")
    print("1. Add an Expenses")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Filter Expenses")
    print("5. Monthly summary")
    print("6. Total spent")
    print("7. Delete an expense")
    print("-----------------------------")


def main():
    print("Welcome to expense tracker")
    show_menu()
    print("\n")
    expenses = load_expenses()

    for expense in expenses:
        print("Title - Amount - Category - Date")
        print(
            expense["title"],
            " - ",
            expense["amount"],
            " - ",
            expense["category"],
            " - ",
            expense["date"],
        )

    while True:
        option = input("\nEnter the Menu Option Number: ")
        if option == "1":
            expense_id = len(expenses) + 1 if len(expenses) > 1 else 1
            title = input("Enter the Name of the Item ex-(Apple): ")
            amount = int(input("Enter the Amount: "))

            print("\n -------- Category ----------")
            print("1. Food")
            print("2. House")
            print("3. Outdoor")
            print("4. Others")
            print("-------------------------------\n")

            date = input("Enter the Date")
            category = input("Select the Category: ")
            expenses.append(
                {"id": expense_id, "title": title, "amount": amount, "date": date}
            )

        else:
            break


if __name__ == "__main__":
    main()
