from core.detect_csv_files import *
from core.detect_user_type import *
from dashboards.moderator_dashboard import *
from dashboards.librarian_dashboard import *
from dashboards.accountant_dashboard import *
from dashboards.admin_dashboard import *
from dashboards.developer_dashboard import *
from dashboards.exam_coordinator_dashboard import *
from dashboards.institute_admin_dashboard import *
from dashboards.it_admin_dashboard import *
from dashboards.parent_dashboard import *
from dashboards.teacher_dashboard import *
from dashboards.student_dashboard import *
from dashboards.super_admin_dashboard import *
from auth.otp import *
from auth.signup import *


def log_login(uid,user_type,status):
    df = pd.read_csv(LOGIN_HISTORY_CSV)
    df.loc[len(df)] = [uid,user_type,datetime.now().strftime("%Y-%m-%d %H:%M:%S"),status]
    df.to_csv(LOGIN_HISTORY_CSV,index=False)

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
