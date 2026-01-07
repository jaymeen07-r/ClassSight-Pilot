import datetime
from core.detect_csv_files import *

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