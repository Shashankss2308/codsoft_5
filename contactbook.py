
def show_menu():
    print("\nContact Book Menu:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def display_contacts(contact_book):
    if contact_book=={}:
        print("\nYour contact book is empty.")
    else:
        print("\nYour Contacts:")
        for key in contact_book.keys():
            print(key, contact_book[key])

def main():
    contact_book = {} # Dictionary to store contacts

    while True:
        show_menu()
        choice = input("Enter your choice 1-5: ")

        if choice == "1":
            display_contacts(contact_book)

        elif choice == "2":
            name = input("Enter the name: ")
            det =input("Enter the contact number, email and city address ")
            detail = det.split(',')
            contact_book[name] = detail
            print("Contact added.")

        elif choice == "3":
            search_name = input("Enter the name to search: ")
            if search_name in contact_book.keys():
                print("Name:",search_name, " Number:",contact_book[search_name])
            else:
                print("Contact not found.")

        elif choice == "4":
            delete_name = input("Enter the name of the contact to delete: ")
            if delete_name in contact_book.keys():
                del contact_book[delete_name]
                print(delete_name," Contact deleted")
            else:
                print("Contact not found.")

        elif choice == "5":
            print("Exiting Contact Book")
            break

        else:
            print("Invalid choice, Enter a number between 1-5.")

main()