from core.detect_csv_files import *

def parent_dashboard(uid):
    df_par = pd.read_csv(PARENTS_CSV)
    parent = df_par[df_par["parent_uid"]==uid].iloc[0]
    student_uid = parent["student_uid"]
    uid = parent["parent_uid"]
    while True:
        print(f"\n=== PARENT DASHBOARD ({parent['parent_name']}) ===")
        print("1. View Child Profile")
        print("2. View Child Academic Report")
        print("3. Send Message to Teacher")
        print("4. Logout")
        choice = input("Choose: ").strip()
        if choice=="1":
            df_stu = pd.read_csv(STUDENTS_CSV)
            student = df_stu[df_stu["uid"]==student_uid].iloc[0]
            print(student.to_string())
        elif choice=="2":
            df_stu = pd.read_csv(STUDENTS_CSV)
            student = df_stu[df_stu["uid"]==student_uid].iloc[0]
            print(student[["maths","science","english","ss","gujarati","computer"]])
        elif choice=="3":
            messagenow(uid)
        elif choice=="4":
            break
        else:
            print("Invalid choice!")