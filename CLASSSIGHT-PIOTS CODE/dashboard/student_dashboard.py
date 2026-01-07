from core.detect_csv_files import *

def student_dashboard(uid):
    df = pd.read_csv(STUDENTS_CSV)
    student = df[df["uid"]==uid].iloc[0]
    while True:
        print(f"\n=== STUDENT DASHBOARD ({student['name']}) ===")
        print("1. View Profile")
        print("2. View Academic Report")
        print("3. View Attendance")
        print("4. Logout")
        choice = input("Choose: ").strip()
        if choice=="1":
            print(student.to_string())
        elif choice=="2":
            print(student[["maths","science","english","ss","gujarati","computer"]])
            total = sum([int(student[sub]) for sub in ["maths","science","english","ss","gujarati","computer"]])
            print(f"Total: {total}")
        elif choice=="3":
            print(f"Attendance: {student['attendance']}%")
        elif choice=="4":
            break
        else:
            print("Invalid choice!")