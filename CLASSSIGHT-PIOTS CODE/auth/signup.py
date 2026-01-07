from core.detect_csv_files import *

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