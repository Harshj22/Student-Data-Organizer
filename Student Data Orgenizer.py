print("🎓 Welcome to the Simple Student Data Organizer!\n")

students = [] 
while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Subjects")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # 1️⃣ Add Student
    if choice == '1':
        print("\n--- Add Student Details ---")
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        subjects = []
        print("Enter 3 Subjects:")
        for i in range(3):
            sub = input(f"Subject {i+1}: ")
            subjects.append(sub)

        id_dob = (sid, dob)         
        subject_set = set(subjects)

        # dictionary for 1 student
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subject_set
        }

        students.append(student)
        print("\n✅ Student added successfully!")

    # 2️⃣ Show All Students
    elif choice == '2':
        if len(students) == 0:
            print("\n❌ No student data found!")
        else:
            print("\n--- All Students ---")
            for s in students:
                print(f"\nStudent ID: {s['id_dob'][0]}")
                print(f"Date of Birth: {s['id_dob'][1]}")
                print(f"Name: {s['name']}")
                print(f"Age: {s['age']}")
                print(f"Grade: {s['grade']}")
                print(f"Subjects: {', '.join(s['subjects'])}")

    # 3️⃣ Update Student
    elif choice == '3':
        sid = input("Enter Student ID to update: ")
        found = False

        for s in students:
            if s['id_dob'][0] == sid:
                found = True
                print("\nWhat do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Grade")
                print("4. Subjects")

                up = input("Enter your choice: ")

                if up == '1':
                    s['name'] = input("Enter new name: ")
                elif up == '2':
                    s['age'] = input("Enter new age: ")
                elif up == '3':
                    s['grade'] = input("Enter new grade: ")
                elif up == '4':
                    new_subs = []
                    print("Enter new 3 subjects:")
                    for i in range(3):
                        sub = input(f"Subject {i+1}: ")
                        new_subs.append(sub)
                    s['subjects'] = set(new_subs)
                else:
                    print("❌ Invalid choice!")
                print("✅ Data updated successfully!")
                break

        if not found:
            print("❌ Student ID not found!")

    # 4️⃣ Delete Student
    elif choice == '4':
        sid = input("Enter Student ID to delete: ")
        deleted = False
        for s in students:
            if s['id_dob'][0] == sid:
                students.remove(s)
                deleted = True
                print("✅ Student deleted successfully!")
                break
        if not deleted:
            print("❌ Student not found!")

    # 5️⃣ Show All Subjects
    elif choice == '5':
        all_subs = set()
        for s in students:
            all_subs.update(s['subjects'])
        if len(all_subs) == 0:
            print("❌ No subjects found!")
        else:
            print("\nAll Subjects Offered:", ", ".join(all_subs))

    # 6️⃣ Exit
    elif choice == '6':
        print("\n👋 Thank you for using the Student Data Organizer!")
        break

    else:
        print("❌ Invalid choice! Please enter between 1 to 6.")
