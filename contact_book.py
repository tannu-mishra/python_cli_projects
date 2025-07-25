# contact_book.py

print("📱 Welcome to Contact Book CLI App")

# Empty contact dictionary
contacts = {}

# Infinite loop for menu
while True:
    print("\nMain Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"✅ {name} added successfully.")

    elif choice == "2":
        if contacts:
            print("\n📒 Your Contacts:")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")
        else:
            print("❌ No contacts found.")

    elif choice == "3":
        search_name = input("Enter name to search: ").strip()
        if search_name in contacts:
            print(f"🔍 Found: {search_name} → {contacts[search_name]}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        del_name = input("Enter name to delete: ").strip()
        if del_name in contacts:
            del contacts[del_name]
            print(f"🗑️ {del_name} deleted.")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter 1–5.")
