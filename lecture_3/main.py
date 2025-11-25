students = []   # список студентов

while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report")
    print("4. Find top performer")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    #OPTION 1
    if choice == "1":
        name = input("Enter student name: ")

        # проверяем, есть ли студент
        exists = False
        for s in students:
            if s["name"].lower() == name.lower():
                exists = True
                break

        if exists:
            print("Such student already exists.")
        else:
            students.append({"name": name, "grades": []})
            print("Student added.")


    #OPTION 2
    elif choice == "2":
        name = input("Enter student name: ")

        # ищем студента
        found = None
        for s in students:
            if s["name"].lower() == name.lower():
                found = s
                break

        if found is None:
            print("Student not found.")
        else:
            print("Enter grades (0–100). Type 'done' to finish.")

            while True:
                g = input("Grade: ")

                if g.lower() == "done":
                    break

                try:
                    grade = int(g)
                    if 0 <= grade <= 100:
                        found["grades"].append(grade)
                        print("Grade added.")
                    else:
                        print("Grade must be 0–100.")
                except:
                    print("Invalid grade.")


    #OPTION 3
    elif choice == "3":
        if not students:
            print("No students yet.")
            continue

        print("\n--- REPORT ---")
        averages = []

        for s in students:
            if len(s["grades"]) == 0:
                print(f"{s['name']} — average: N/A")
            else:
                avg = sum(s["grades"]) / len(s["grades"])
                averages.append(avg)
                print(f"{s['name']} — average: {avg:.2f}")

        if averages:
            print("\nMax average:", max(averages))
            print("Min average:", min(averages))
            print("Overall average:", sum(averages)/len(averages))
        else:
            print("No grades added yet.")


    #OPTION 4
    elif choice == "4":
        top_student = None
        top_avg = -1

        for s in students:
            if s["grades"]:
                avg = sum(s["grades"]) / len(s["grades"])
                if avg > top_avg:
                    top_avg = avg
                    top_student = s

        if top_student is None:
            print("No students with grades.")
        else:
            print(f"Top performer: {top_student['name']} ({top_avg:.2f})")


    #OPTION 5
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")