import json


def menu():
    print("Welcome to Contact Book App: ")
    show_menu()
    print("\n")

    while True:
        print("--------Loaded Data----------")
        contact_list = load_contacts()  # Load the Contacts List

        print("Id - Name - Phone - Email - Address")
        for contact in contact_list:
            print(
                contact["id"],
                "-",
                contact["name"],
                "-",
                contact["phone"],
                "-",
                contact["email"],
                "-",
                contact["address"],
            )
        print("-----------------------------")
        option = input("Enter the Number from the Menu List: ")

        if option == "1":  # Add contact
            add_contact(contact_list)
            if not close():
                break

        elif option == "2":  # View Contacts list
            view_contacts(contact_list)
            if not close():
                break

        elif option == "3":
            search_contact(contact_list)
            if not close():
                break

        elif option == "4":
            update_contact(contact_list)
            if not close():
                break

        elif option == "5":
            delete_contact(contact_list)
            if not close():
                break

        else:
            break


def load_contacts():
    with open("contacts.json", "r") as file:
        return json.load(file)


def save_contacts(list):
    with open("contacts.json", "w") as file:
        json.dump(list, file, indent=4)


def add_contact(contact_list):
    contact_id = len(contact_list) + 1 if len(contact_list) > 0 else 1
    contact_name = input("Enter the Name: ")
    contact_phone = int(input("Enter the Phone Number: "))
    contact_email = input("Enter the Email Address: ")
    contact_address = input("Enter the Address: ")
    contact_list.append(
        {
            "id": contact_id,
            "name": contact_name,
            "phone": contact_phone,
            "email": contact_email,
            "address": contact_address,
        }
    )
    save_contacts(contact_list)


def view_contacts(contact_list):
    print("------------- View Mode ----------------")
    print("Id - Name - Phone - Email - Address")
    for contact in contact_list:
        print(
            contact["id"],
            "-",
            contact["name"],
            "-",
            contact["phone"],
            "-",
            contact["email"],
            "-",
            contact["address"],
        )
    print("---------------------------------------")


def search_contact(contacts):
    keywords = input("Enter name/phone/email you want to search: ").lower()
    found = False

    for contact in contacts:
        if (
            keywords in contact["name"].lower()
            or keywords in contact["phone"]
            or keywords in contact["email"].lower()
        ):

            print("\n--- Contact Found ---")
            print(f"name: {contact['name']}")
            print(f"phone: {contact['phone']}")
            print(f"email: {contact['email']}")
            found = True

        if not found:
            print("\n❌ No matching contact found.")


def update_contact(contacts):
    print("1. Name")
    print("2. Email")
    print("3. Phone")
    print("4. Address")

    try:
        update_type = input("Enter the Option to which you want to update: ")
        update_key = int(input("Enter the Key: "))

        # Check if Key exists
        if any(update_key == contact["id"] for contact in contacts):
            for contact in contacts:
                if contact["id"] == update_key:
                    if update_type == "1":
                        data = input("Enter the Name to Update: ")
                        contact["name"] = data
                    elif update_type == "2":
                        data = input("Enter the Email to Update: ")
                        contact["email"] = data
                    elif update_type == "3":
                        data = int(input("Enter the Phone Number to Update: "))
                        contact["phone"] = data
                    elif update_type == "4":
                        data = input("Enter the Address to Update: ")
                        contact["address"] = data
                    else:
                        print("\n No Such Update Option Available")
            save_contacts(contacts)
        else:
            print("No Such Key found")
    except ValueError:
        print("Please Enter the Correct Value: ")


def delete_contact(contacts):
    contact_id = int(input("Enter the Contact ID you want to delete: "))
    # Check if the id exits
    if any(contact_id == contact["id"] for contact in contacts):
        confirmation = input("Are you sure you want to delete the Contact: y/n  ")

        if confirmation == "y":
            # filter the contacts
            filtered_contact = filter(lambda x: x["id"] != contact_id, contacts)
            save_contacts(list(filtered_contact))
    else:
        print("\n No Such Key exits in the Contact List")


def show_menu():
    print("--------Menu List---------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contacts")
    print("5. Delete Contact")
    print("--------------------------")


def close():
    is_close = input("Do you want to continue y/n: ")
    return is_close == "y"


if __name__ == "__main__":
    menu()
