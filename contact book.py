# Initialize an empty dictionary to store contacts
contact_book = {}

# Function to add a new contact
def add_contact(name, phone, email):
    contact_book[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

# Function to search for a contact by name
def search_contact(name):
    contact = contact_book.get(name)
    if contact:
        print(f"Found contact - Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        print(f"Contact '{name}' not found.")

# Function to update an existing contact
def update_contact(name, phone=None, email=None):
    if name in contact_book:
        if phone:
            contact_book[name]["Phone"] = phone
        if email:
            contact_book[name]["Email"] = email
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Main menu to interact with the contact book
def contact_book_app():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the contact book app
contact_book_app()
