def basic_calculator():
    print(
        "Welcome to the basic calculator, with operation like Add, Sub, Multiple, and Divide"
    )

    while True:
        try:
            show_menu()
            type_of_operation = int(input("Select the Option, provide the number: "))

            if type_of_operation < 1 or type_of_operation > 5:
                print(
                    "Please try again, the option should be from 1 to 5 as shown in the menu"
                )
            
            a_value = int(input("Select the first number: "))
            b_value = int(input("Select the Second number: "))

            if type_of_operation == 1:
                print("Addition", add(a_value, b_value))
                check = check_task()

                if check == "n":
                    break
            elif type_of_operation == 2:
                print("Subtraction", sub(a_value, b_value))
                check = check_task()

                if check == "n":
                    break
            elif type_of_operation == 3:
                print("Multiply", multiply(a_value, b_value))
                check = check_task()

                if check == "n":
                    break
            elif type_of_operation == 4:
                print("Divide", divide(a_value, b_value))
                check = check_task()

                if check == "n":
                    break
            else:
                break

        except ValueError:
            print("Please Select the Number")


def show_menu():
    print("------ Calculator Menu ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-----------------------------")

def check_task():
    return input("Do you want to calculate again? (y/n): ")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == "__main__":
    basic_calculator()
