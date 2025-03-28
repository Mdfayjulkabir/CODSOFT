# Contact Book 

import re

class ContactBook:
    def __init__(self):
        self.contacts = {}

    # Email validation function to ensure it ends with @gmail.com
    def validate_email(self, email):
        # Regex pattern to check for a valid email format ending with @gmail.com
        email_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
        if re.match(email_pattern, email):
            return True
        else:
            print("Invalid Gmail address. Please provide a valid email ending with @gmail.com.")
            return False

    # Add a new contact
    def add_contact(self):
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        

        while True:
            email = input("Enter the contact's email (must end with @gmail.com): ")
            if self.validate_email(email):
                break 
        
        address = input("Enter the contact's address: ")

        # Store contact information
        self.contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact for {name} has been added.")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"{name} - {details['Phone']}")

    # Search for a contact by name or phone
    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ")
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["Phone"]:
                print(f"\n{name}:")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                found = True
        if not found:
            print("No contact found.")

    # Update an existing contact
    def update_contact(self):
        name = input("Enter the contact's name to update: ")
        if name in self.contacts:
            print(f"Updating contact for {name}:")
            phone = input("Enter the new phone number: ")
            
            # Loop until a valid Gmail is entered
            while True:
                email = input("Enter the new email (must end with @gmail.com): ")
                if self.validate_email(email):
                    break  # Exit loop once valid Gmail is entered
            
            address = input("Enter the new address: ")

            # Update the contact details
            self.contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            print(f"Contact for {name} has been updated.")
        else:
            print("Contact not found.")

    # Delete a contact
    def delete_contact(self):
        name = input("Enter the contact's name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} has been deleted.")
        else:
            print("Contact not found.")

    # User Interface 
    def user_interface(self):
        while True:
            print("\nContact Book")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Select an option (1-6): ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Start the contact book
if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.user_interface()
