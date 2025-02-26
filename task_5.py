contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added!\n")

def view_contacts():
    for contact in contacts:
        print(contact["name"], "-", contact["phone"])
    print()

def search_contact():
    query = input("Search: ")
    for contact in contacts:
        if query in contact.values():
            print(contact["name"], "-", contact["phone"])
    print()

def delete_contact():
    query = input("Delete: ")
    for contact in contacts:
        if query in contact.values():
            contacts.remove(contact)
            print("Deleted!\n")
            return
    print("Not found.\n")

def main():
    while True:
        choice = input("select from following choices 1:Add 2:View 3:Search 4:Delete 5:Exit\n")
        if choice == "1": add_contact()
        elif choice == "2": view_contacts()
        elif choice == "3": search_contact()
        elif choice == "4": delete_contact()
        elif choice == "5": break
        else: print("Invalid choice!\n")

main()
