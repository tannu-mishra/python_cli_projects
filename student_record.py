print("🎓 Welcome to Student Record Management System")

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    std_class = input("Enter Class: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{std_class},{marks}\n")

    print("✅ Student added successfully!\n")

def view_students():
    try:
        with open("students.txt", "r") as file:
            print("\n📋 Student Records:\n")
            for line in file:
                name, roll, std_class, marks = line.strip().split(",")
                print(f"Name: {name}, Roll: {roll}, Class: {std_class}, Marks: {marks}")
    except FileNotFoundError:
        print("⚠️ No records found.\n")

def search_student():
    roll_to_search = input("Enter Roll Number to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, std_class, marks = line.strip().split(",")
                if roll == roll_to_search:
                    print(f"\n🎯 Student Found:\nName: {name}, Roll: {roll}, Class: {std_class}, Marks: {marks}\n")
                    found = True
                    break
        if not found:
            print("❌ Student not found.\n")
    except FileNotFoundError:
        print("⚠️ No records available.\n")

# Main Menu
while True:
    print("\n==== MENU ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
