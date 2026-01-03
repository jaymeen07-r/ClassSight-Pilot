import pandas as pd
import os
import random
import string
from messaging_system import *
from datetime import datetime


STUDENTS_CSV = "students.csv"
PARENTS_CSV = "parents.csv"
TEACHERS_CSV = "teachers.csv"
MESSAGES_CSV = "messages.csv"
LOGIN_HISTORY_CSV = "login_history.csv"


def ensure_csv_files():
    if not os.path.exists(STUDENTS_CSV):
        pd.DataFrame(columns=["uid","name","class","roll_no","password",
                              "maths","science","english","ss","gujarati","computer",
                              "attendance"]).to_csv(STUDENTS_CSV,index=False)
    if not os.path.exists(PARENTS_CSV):
        pd.DataFrame(columns=["parent_uid","student_uid","parent_name","password","phone"]).to_csv(PARENTS_CSV,index=False)
    if not os.path.exists(TEACHERS_CSV):
        pd.DataFrame(columns=["teacher_uid","name","class_assigned","password","phone"]).to_csv(TEACHERS_CSV,index=False)
    if not os.path.exists(MESSAGES_CSV):
        pd.DataFrame(columns=["from_uid","to_uid","message","timestamp"]).to_csv(MESSAGES_CSV,index=False)
    if not os.path.exists(LOGIN_HISTORY_CSV):
        pd.DataFrame(columns=["uid","user_type","login_time","status"]).to_csv(LOGIN_HISTORY_CSV,index=False)
    if not pd.io.common.file_exists(STUDENTS_CSV):
        pd.DataFrame(columns=["uid","name","class","roll_no","password",
                              "maths","science","english","ss","gujarati","computer","attendance"]).to_csv(STUDENTS_CSV,index=False)
    if not pd.io.common.file_exists(PARENTS_CSV):
        pd.DataFrame(columns=["parent_uid","student_uid","parent_name","password","phone"]).to_csv(PARENTS_CSV,index=False)


def generate_random_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_otp():
    return str(random.randint(100000,999999))


def log_login(uid,user_type,status):
    df = pd.read_csv(LOGIN_HISTORY_CSV)
    df.loc[len(df)] = [uid,user_type,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),status]
    df.to_csv(LOGIN_HISTORY_CSV,index=False)


def detect_user_type(uid):
    uid = uid.strip()
    if uid.lower() == "schoolmod":
        return "moderator"
    elif len(uid) == 6 and uid.startswith("SA") and uid[2:].isdigit():
        return "super_admin"

    elif len(uid) == 7 and uid.startswith("ADM") and uid[3:].isdigit():
        return "institute_admin"

    elif len(uid) == 7 and uid.startswith("EXM") and uid[3:].isdigit():
        return "exam_coordinator"

    elif len(uid) == 7 and uid.startswith("LIB") and uid[3:].isdigit():
        return "librarian"

    elif len(uid) == 7 and uid.startswith("ACC") and uid[3:].isdigit():
        return "accountant"

    elif len(uid) == 7 and uid.startswith("ITA") and uid[3:].isdigit():
        return "it_admin"

    elif len(uid) == 7 and uid.startswith("DEV") and uid[3:].isdigit():
        return "developer"
    elif len(uid) == 7 and uid[:3].upper() == "ADM" and uid[3:].isdigit():
        return "institute_admin"
    elif uid.startswith("P") and len(uid) >= 5:
        return "parent"
    elif len(uid) == 7 and uid[:4].isdigit() and uid[4].isalpha() and uid[5:].isdigit(): 
        return "student"
    elif len(uid) == 8 and uid[:4].isdigit() and uid[4:6].isalpha() and uid[6:].isdigit():
        return "teacher"
    else:
        return "unknown"


def parent_sign_up():
    ensure_csv_files()
    
    print("=== PARENT SIGN-UP ===")
    parent_name = input("Enter Parent Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    student_uid = input("Enter Student UID: ").strip()
    student_pw = input("Enter Student Password: ").strip()
    
 
    df_students = pd.read_csv(STUDENTS_CSV)
    if student_uid not in df_students["uid"].values:
        print("Student UID not found. Cannot create parent account.")
        return
    
    real_student_pw = df_students[df_students["uid"]==student_uid]["password"].values[0]
    if student_pw != real_student_pw:
        print("Student password incorrect. Cannot create parent account.")
        return
    
    roll_no = student_uid[-2:]
    div = student_uid[4]
    class_num = student_uid[2:4]
    parent_uid = f"P{roll_no}{div}{class_num}"
    

    df_parents = pd.read_csv(PARENTS_CSV)
    if parent_uid in df_parents["parent_uid"].values:
        print(f"Parent account already exists. UID: {parent_uid}")
        return
    

    password = input("Set your Parent Account Password: ").strip()
    

    otp = generate_otp()
    print(f"OTP sent to registered phone/email: {otp}") 
    entered_otp = input("Enter OTP: ").strip()
    if entered_otp != otp:
        print("OTP verification failed. Sign-Up aborted.")
        return

    new_parent = {
        "parent_uid": parent_uid,
        "student_uid": student_uid,
        "parent_name": parent_name,
        "password": password,
        "phone": phone
    }
    df_parents = pd.concat([df_parents, pd.DataFrame([new_parent])], ignore_index=True)
    df_parents.to_csv(PARENTS_CSV,index=False)
    
    print(f"Parent account created successfully! UID: {parent_uid}")

    
def otp_verification(uid):
    otp = generate_otp()
    print(f"OTP sent to registered mobile/email for {uid}: {otp}")
    entered = input("Enter OTP: ").strip()
    if entered == otp:
        print("OTP verified successfully!")
        return True
    else:
        print("OTP verification failed.")
        return False


def moderator_dashboard():
    while True:
        print("\n=== MODERATOR DASHBOARD ===")
        print("1. Create Teacher Account")
        print("2. View Teachers")
        print("3. Exit Moderator Dashboard")
        choice = input("Choose: ").strip()
        if choice == "1":
            create_teacher_account()
        elif choice == "2":
            df = pd.read_csv(TEACHERS_CSV)
            print(df.to_string(index=False))
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def create_teacher_account():
    name = input("Enter Teacher Name: ").strip()
    class_assigned = input("Class assigned (e.g., 10A): ").strip()
    year = datetime.now().year % 100
    rand_num = random.randint(10,99)
    uid = f"{year}{rand_num}{name[0].upper()}{name[-1].upper()}01"
    password = generate_random_password()
    phone = input("Enter phone number: ").strip()
    df = pd.read_csv(TEACHERS_CSV)
    df.loc[len(df)] = [uid,name,class_assigned,password,phone]
    df.to_csv(TEACHERS_CSV,index=False)
    print(f"Teacher account created. UID: {uid}, Password: {password}")
    print("Credentials will be auto-sent to teacher (simulate here).")


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


def add_new_student(class_assigned):
    name = input("Enter Student Name: ").strip()
    roll_no = input("Enter Roll No: ").strip()
    
    year = datetime.now().year % 100
    class_num = class_assigned[:-1]
    div = class_assigned[-1].upper()
    
    uid = f"{year}{class_num}{div}{roll_no.zfill(2)}"
    password = generate_random_password()

    df = pd.read_csv(STUDENTS_CSV)
    
    required_columns = ["uid","name","class","roll_no","password",
                        "maths","science","english","ss","gujarati","computer","attendance"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0

    new_student = {
        "uid": uid,
        "name": name,
        "class": class_assigned,
        "roll_no": roll_no,
        "password": password,
        "maths": 0,
        "science": 0,
        "english": 0,
        "ss": 0,
        "gujarati": 0,
        "computer": 0,
        "attendance": 0
    }

    df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
    df.to_csv(STUDENTS_CSV,index=False)

    print(f"Student account created. UID: {uid}, Temporary Password: {password}")
    print("Send student credentials to parent automatically via system.")


def edit_student_marks(class_assigned):
    df = pd.read_csv(STUDENTS_CSV)
    class_students = df[df["class"]==class_assigned]
    print(class_students[["uid","name","roll_no"]].to_string(index=False))
    uid = input("Enter Student UID to edit marks: ").strip()
    if uid not in class_students["uid"].values:
        print("Invalid UID")
        return
    subjects = ["maths","science","english","ss","gujarati","computer"]
    for sub in subjects:
        marks = input(f"Enter marks for {sub}: ").strip()
        df.loc[df["uid"]==uid,sub] = int(marks)
    df.to_csv(STUDENTS_CSV,index=False)
    print("Marks updated successfully.")


def view_class_report(class_assigned):
    df = pd.read_csv(STUDENTS_CSV)
    class_students = df[df["class"]==class_assigned]
    print(class_students.to_string(index=False))


def send_message_teacher_to_parent():
    from_uid = input("Enter your Teacher UID: ").strip()
    to_uid = input("Enter Parent UID: ").strip()
    message = input("Enter Message: ").strip()
    df = pd.read_csv(MESSAGES_CSV)
    df.loc[len(df)] = [from_uid,to_uid,message,datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    df.to_csv(MESSAGES_CSV,index=False)
    print("Message sent successfully.")


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


def super_admin_dashboard():
    print("\n=== SUPER ADMIN DASHBOARD ===")
    print("1. Manage All Institutes")
    print("2. Manage All Users (Admins/Teachers/Students)")
    print("3. System Analytics")
    print("4. Approve High-Level Reports")
    print("5. Broadcast System Notices")
    print("6. Global Settings & Configurations")
    print("7. Data Backup & Restore")
    print("8. API / Integrations")
    print("0. Logout")

    choice = input("Choose: ").strip()
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        super_admin_dashboard()


def institute_admin_dashboard():
    print("\n=== INSTITUTE ADMIN DASHBOARD ===")
    print("1. Manage Teachers / Students / Parents")
    print("2. Approve AI-Generated Reports")
    print("3. Generate Notice / Official Documents")
    print("4. Approve Exam Schedules / Reports")
    print("5. Auto-Generate Progress Reports")
    print("6. Manage Templates (Certificates / Reports)")
    print("7. View Institute-Wide Analytics")
    print("8. Track Teacher Performance")
    print("9. Attendance Analytics")
    print("10. Custom Letter / Document Generator")
    print("0. Logout")

    choice = input("Choose an option: ").strip()

    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        institute_admin_dashboard()


def developer_dashboard():
    print("\n=== DEVELOPER DASHBOARD ===")
    print("1. API Access Keys")
    print("2. Webhooks & Integrations")
    print("3. System Logs")
    print("4. Feature Testing Sandbox")
    print("5. Deploy Updates")
    print("6. Debug Mode")
    print("0. Logout")

    choice = input("Choosean option: ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        developer_dashboard()


def it_admin_dashboard():
    print("\n=== IT ADMIN DASHBOARD ===")
    print("1. System Configuration")
    print("2. Security Settings")
    print("3. API Integrations")
    print("4. User Access Management")
    print("5. Network Monitoring")
    print("6. Log Viewer / Debug Tools")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        it_admin_dashboard()


def accountant_dashboard():
    print("\n=== ACCOUNTANT / FEE MANAGER DASHBOARD ===")
    print("1. Fee Tracking")
    print("2. Payment History")
    print("3. Salary Statements")
    print("4. Financial Reports")
    print("5. Manage Discounts / Scholarships")
    print("6. Auto-Generate Fee Receipts")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()

    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        accountant_dashboard()


def librarian_dashboard():
    print("\n=== LIBRARIAN DASHBOARD ===")
    print("1. Book Issue / Return")
    print("2. Track Library Usage")
    print("3. Student Reading Analytics")
    print("4. Add / Remove Books")
    print("5. Fine Management")
    print("6. Generate Library Reports")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        librarian_dashboard()


def exam_coordinator_dashboard():
    print("\n=== EXAM COORDINATOR DASHBOARD ===")
    print("1. Create Exam Timetables")
    print("2. Manage Marksheets")
    print("3. AI-Based Result Analysis")
    print("4. Approve Results")
    print("5. Generate Reports & Certificates")
    print("6. Student Performance Comparison")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        exam_coordinator_dashboard()


def login_or_signup():
    ensure_csv_files()
    print("=== Welcome to School Assistant ===")
    print("1. Login")
    print("2. Parent Sign-Up")
    print("3. Exit")
    choice = input("Choose: ").strip()
    if choice=="1":
        uid = input("Enter UID: ").strip()
        user_type = detect_user_type(uid)
        if user_type=="unknown":
            print("Invalid UID format.")
            return
        if user_type=="moderator":
            pw = input("Enter password: ").strip()
            if pw=="jaymeen07-r":
                print("Moderator login successful!")
                moderator_dashboard()
            else:
                print("Invalid password!")
            return
        
        elif user_type == "super_admin":
            pw = input("Enter password: ").strip()
            if pw == "super@123":
                print("Super Admin login successful!")
                super_admin_dashboard()
            else:
                print("Invalid password!")
            return
        
        elif user_type == "librarian":
            pw = input("Enter password: ").strip()
            if pw == "lib@123":
                print("Librarian login successful!")
                librarian_dashboard()
            else:
                print("Invalid password!")
            return

        elif user_type == "accountant":
            pw = input("Enter password: ").strip()
            if pw == "acc@123":
                print("Accountant login successful!")
                accountant_dashboard()
            else:
                print("Invalid password!")
            return

        elif user_type == "it_admin":
            pw = input("Enter password: ").strip()
            if pw == "it@123":
                print("IT Admin login successful!")
                it_admin_dashboard()
            else:
                print("Invalid password!")
            return

        elif user_type == "developer":
            pw = input("Enter password: ").strip()
            if pw == "dev@123":
                print("Developer login successful!")
                developer_dashboard()
            else:
                print("Invalid password!")
            return

        elif user_type == "exam_coordinator":
            pw = input("Enter password: ").strip()
            if pw == "exam@123":
                print("Exam Coordinator login successful!")
                exam_coordinator_dashboard()
            else:
                print("Invalid password!")
            return
        
        elif user_type == "institute_admin":
            pw = input("Enter password: ").strip()
            if pw == "admin@123":   
                print("Institute Admin login successful!")
                institute_admin_dashboard()
            else:
                print("Invalid password!")
            return

        elif user_type=="student":
            student_login(uid)
        elif user_type=="parent":
            parent_login(uid)
        elif user_type=="teacher":
            teacher_login(uid)
    if choice=="2":
        parent_sign_up()
    else:
        print("Exiting...")


def student_login(uid):
    df = pd.read_csv(STUDENTS_CSV)
    if uid not in df["uid"].values:
        print("Student UID not found.")
        return
    temp_pass = df[df["uid"]==uid]["password"].values[0]
    pw = input("Enter password: ").strip()
    if pw!=temp_pass:
        print("Incorrect password.")
        log_login(uid,"student","failed")
        return
    print("Password correct. Please verify OTP.")
    if otp_verification(uid):
        new_pw = input("Set your new password: ").strip()
        df.loc[df["uid"]==uid,"password"] = new_pw
        df.to_csv(STUDENTS_CSV,index=False)
        log_login(uid,"student","success")
        print("Password set successfully! Redirecting to dashboard...")
        student_dashboard(uid)
    else:
        log_login(uid,"student","failed")


def parent_login(uid=None):
    df = pd.read_csv(PARENTS_CSV)
    if uid is None:
        name = input("Enter Parent Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        student_uid = input("Enter Student UID: ").strip()
        student_pw = input("Enter Student Password: ").strip()
        df_stu = pd.read_csv(STUDENTS_CSV)
        if student_uid not in df_stu["uid"].values or df_stu[df_stu["uid"]==student_uid]["password"].values[0]!=student_pw:
            print("Invalid student credentials.")
            return
        parent_uid = f"P{student_uid[-2:]}{student_uid[4]}{student_uid[:2]}"
        new_pw = input("Set your parent account password: ").strip()
        df.loc[len(df)] = [parent_uid,student_uid,name,new_pw,phone]
        df.to_csv(PARENTS_CSV,index=False)
        print(f"Parent account created. UID: {parent_uid}")
        parent_login(parent_uid)
        return
    pw = input("Enter password: ").strip()
    if uid not in df["parent_uid"].values:
        print("Parent UID not found.")
        log_login(uid,"parent","failed")
        return
    real_pw = df[df["parent_uid"]==uid]["password"].values[0]
    if pw!=real_pw:
        print("Incorrect password.")
        log_login(uid,"parent","failed")
        return
    print("Password correct. Please verify OTP.")
    if otp_verification(uid):
        log_login(uid,"parent","success")
        parent_dashboard(uid)
    else:
        log_login(uid,"parent","failed")


def teacher_login(uid):
    df = pd.read_csv(TEACHERS_CSV)
    if uid not in df["teacher_uid"].values:
        print("Teacher UID not found.")
        return
    pw = input("Enter password: ").strip()
    real_pw = df[df["teacher_uid"]==uid]["password"].values[0]
    if pw!=real_pw:
        print("Incorrect password.")
        log_login(uid,"teacher","failed")
        return
    print("Password correct. Verify OTP to continue.")
    if otp_verification(uid):
        log_login(uid,"teacher","success")
        teacher_dashboard(uid)
    else:
        log_login(uid,"teacher","failed")


if __name__=="__main__":
    while True:
        login_or_signup()
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont!="y":
            print("Exiting system...")
            break