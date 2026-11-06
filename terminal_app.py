from contact_manager import ContactManager
from faker import Faker

def load_sample_contacts(manager, count=100):
    """"generate fake contacts using Faker and add them to the manager"""
    fake = Faker()
    added = 0
    for _ in range(count):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        if manager.add_contact(name, phone, email):
            added += 1
    print(f"✅ Loaded {added} sample contacts out of |{count} generated")

def display_menu():
    print("\n" + "=" * 40)
    print("      CONTACT MANAGER - TERMINAL MENU")
    print("=" * 40)
    print("1. Add new contact")
    print("2. Search contact by name")
    print("3. Delete contact")
    print("4. List all contacts")
    print("5. Load 100 sample contacts (Faker)")
    print("0. Exit")
    print("=" * 40)

def main():
    manager = ContactManager()
    print("Welcome to Contact Manager")

    while True:
        display_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            name = input("Enter full name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            if not name or not phone or not email:
                print("❌ All fields are required.")
                continue
            success = manager.add_contact(name, phone, email)
            if success:
                print(f"✅ Contact '{name}' added successfully!")
            else:
                print(f"❌ Error: A contact named '{name}' already exists.")

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            found = manager.search_contact(name)
            if found:
                print("\n🔍 Contact found:")
                print(found)
            else:
                print(f"❌ No contact found with name '{name}'.")

        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            success = manager.delete_contact(name)
            if success:
                print(f"✅ Contact '{name}' deleted successfully.")
            else:
                print(f"❌ No contact found with name '{name}'.")

        elif choice == "4":
            contacts = manager.list_all_contacts()
            if not contacts:
                print("📋 No contacts to display.")
                continue
            print("\n📋 All contacts (sorted):")
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. {contact}")

        elif choice == "5":
            load_sample_contacts(manager, 100)

        elif choice == "0":
            print("👋🏼 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. please try again.")

if __name__ == "__main__":
    main()