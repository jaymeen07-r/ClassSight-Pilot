from core.detect_csv_files import *
from models.students import *
from reports.view_class_report import *

def teacher_dashboard(uid):
    df_teacher = pd.read_csv(TEACHERS_CSV)
    teacher = df_teacher[df_teacher["teacher_uid"]==uid].iloc[0]
    class_assigned = teacher["class_assigned"]
    uid = teacher["teacher_uid"]
    while True:
        print(f"\n=== TEACHER DASHBOARD ({teacher['name']}) ===")
        print("1. Add New Student")
        print("2. Add/Edit Student Marks")
        print("3. View Class Reports")
        print("4. Send Message to Parent")
        print("5. Logout")
        choice = input("Choose: ").strip()
        if choice=="1":
            add_new_student(class_assigned)
        elif choice=="2":
            edit_student_marks(class_assigned)
        elif choice=="3":
            view_class_report(class_assigned)
        elif choice=="4":
            messagenow(uid)
        elif choice=="5":
            break
        else:
            print("Invalid choice!")