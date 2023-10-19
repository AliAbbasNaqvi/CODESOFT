contact = {}  # Define contact as an empty dictionary

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact[key]))

while True:
    choice = int(input(
        "1. Add new contact\n2. Search contact\n3. Display contact\n4. Edit contact\n5. Delete contact\n6. Exit\nEnter your choice: "
    ))

    # add contact
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone  # Add the contact to the dictionary

    # search contact
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not found in the contact book")

    # display contact
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()

    # edit contact
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter mobile number: ")
            contact[edit_contact] = phone  # Update the contact's phone number
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in the contact book")

    # delete contact
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact (yes/no)? ")
            if confirm.lower() == "yes":
                del contact[del_contact]  # Delete the contact
                display_contact()
        else:
            print("Name is not found in the contact book")

    elif choice == 6:
        break
