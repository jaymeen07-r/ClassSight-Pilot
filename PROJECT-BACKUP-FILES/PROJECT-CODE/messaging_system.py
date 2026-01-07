import pandas as pd
import os
from datetime import datetime
import random
import string

STUDENTS_CSV = "students.csv"
PARENTS_CSV = "parents.csv"
TEACHERS_CSV = "teachers.csv"
MESSAGES_CSV = "messages.csv"


def ensure_csv_files():
    
    if not os.path.exists(STUDENTS_CSV):
        pd.DataFrame(columns=[
            "uid","name","class","roll_no","password",
            "maths","science","english","ss","gujarati","computer","attendance"
        ]).to_csv(STUDENTS_CSV, index=False)

 
    if not os.path.exists(PARENTS_CSV):
        pd.DataFrame(columns=[
            "parent_uid","student_uid","parent_name","password","phone"
        ]).to_csv(PARENTS_CSV, index=False)

 
    if not os.path.exists(TEACHERS_CSV):
        pd.DataFrame(columns=[
            "teacher_uid","name","class_assigned","password","phone"
        ]).to_csv(TEACHERS_CSV, index=False)

 
    if not os.path.exists(MESSAGES_CSV):
        pd.DataFrame(columns=["from_uid","to_uid","message","timestamp"]).to_csv(MESSAGES_CSV, index=False)


def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_otp():
    return str(random.randint(100000, 999999))

def generate_random_password(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def read_csv_safe(path):
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str).fillna("")


def get_user_by_name(fullname):
    name_q = fullname.strip().lower()
    df = read_csv_safe(STUDENTS_CSV)
    if not df.empty and "name" in df.columns:
        row = df[df["name"].str.lower() == name_q]
        if not row.empty:
            r = row.iloc[0]
            return {
                "role": "student",
                "uid": r["uid"],
                "name": r["name"],
                "class": r.get("class", ""),
                "roll_no": r.get("roll_no", "")
            }


    df = read_csv_safe(PARENTS_CSV)
    if not df.empty and "parent_name" in df.columns:
        row = df[df["parent_name"].str.lower() == name_q]
        if not row.empty:
            r = row.iloc[0]
            return {
                "role": "parent",
                "uid": r["parent_uid"],
                "name": r["parent_name"],
                "student_uid": r.get("student_uid", ""),
                "phone": r.get("phone", "")
            }

   
    df = read_csv_safe(TEACHERS_CSV)
    if not df.empty and "name" in df.columns:
        row = df[df["name"].str.lower() == name_q]
        if not row.empty:
            r = row.iloc[0]
            return {
                "role": "teacher",
                "uid": r["teacher_uid"],
                "name": r["name"],
                "class_assigned": r.get("class_assigned", ""),
                "phone": r.get("phone", "")
            }

    return None

def get_user_details_by_uid(uid):
    uid = uid.strip()
 
    df = read_csv_safe(STUDENTS_CSV)
    if not df.empty and "uid" in df.columns:
        row = df[df["uid"] == uid]
        if not row.empty:
            r = row.iloc[0]
            return {"role":"student","uid":r["uid"],"name":r["name"],"class":r.get("class",""),"roll_no":r.get("roll_no","")}


    df = read_csv_safe(PARENTS_CSV)
    if not df.empty and "parent_uid" in df.columns:
        row = df[df["parent_uid"] == uid]
        if not row.empty:
            r = row.iloc[0]
            return {"role":"parent","uid":r["parent_uid"],"name":r["parent_name"],"student_uid":r.get("student_uid",""),"phone":r.get("phone","")}


    df = read_csv_safe(TEACHERS_CSV)
    if not df.empty and "teacher_uid" in df.columns:
        row = df[df["teacher_uid"] == uid]
        if not row.empty:
            r = row.iloc[0]
            return {"role":"teacher","uid":r["teacher_uid"],"name":r["name"],"class_assigned":r.get("class_assigned",""),"phone":r.get("phone","")}

    return {"role":"unknown","uid":uid,"name":"Unknown"}

def show_full_user_details(user):
    """
    Prints complete hierarchical user info:
    - full name
    - role
    - children UID & names (if parent)
    - class (if student)
    - phone, email, etc.
    """
    print("\n--- RECIPIENT DETAILS ---")
    

    print(f"Full Name: {user.get('name', 'N/A')}")
    print(f"Role: {user.get('role', 'N/A')}")
    print(f"UID: {user.get('uid', 'N/A')}")
   
    print(f"Phone: {user.get('phone', 'N/A')}")
    print(f"Email: {user.get('email', 'N/A')}")

   
    if user.get("role") == "student":
        print(f"Class: {user.get('class', 'N/A')}")
    
    
    if user.get("role") == "parent":
        children_uids = user.get("children", [])
        if not children_uids and user.get("student_uid"):
        
            children_uids = [user.get("student_uid")]
        
        if children_uids:
            print("\nChildren:")
            for c_uid in children_uids:
                child = get_user_details_by_uid(c_uid)
                if child:
                    print(f"  UID: {child.get('uid', 'N/A')}, Name: {child.get('name', 'N/A')}, Class: {child.get('class', 'N/A')}")
                else:
                    print(f"  UID: {c_uid} (details not found)")
        else:
            print("Children: None")


def send_message(from_uid, to_uid, message_text):
    df = read_csv_safe(MESSAGES_CSV)
    if df.empty:
        df = pd.DataFrame(columns=["from_uid","to_uid","message","timestamp"])
    new_row = {"from_uid": from_uid, "to_uid": to_uid, "message": message_text, "timestamp": now_ts()}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(MESSAGES_CSV, index=False)
    print("Message saved in messages.csv")

def send_message_full_flow(sender_uid):
    print("\n=== SEND MESSAGE ===")
    print("1. Send in group. ")
    print("2. Send to multiple parent. ")
    print("3. send to single parent.")
    c = input("Choose: ").strip()
    if c == "1":
        send_to_multiple(sender_uid)
    elif c == "2":
        send_bulk_messages(sender_uid)
    elif c == "3":
        send_to_single(sender_uid)
   
   
def send_to_multiple(sender_uid):
    df = read_csv_safe(PARENTS_CSV)
    
    if df.empty:
        print("No parents found in database.")
        return

    print(f"\nTotal Parents Found: {len(df)}")
    message_text = input("Enter message to send to ALL parents: ").strip()

    if message_text == "":
        print("Empty message. Aborted.")
        return

    for i, row in df.iterrows():
        parent_uid = row["parent_uid"]
        send_message(sender_uid, parent_uid, message_text)

    print("\n✔ Message successfully sent to ALL parents!")
    
def send_bulk_messages(sender_uid):
    print("\n=== MULTIPLE USER MESSAGE MODE ===")
    names = input("Enter parent names (comma separated): ").strip()

    name_list = [n.strip() for n in names.split(",") if n.strip() != ""]
    if not name_list:
        print("No valid names found.")
        return

    message_text = input("Enter message to send to all: ").strip()
    if message_text == "":
        print("Empty message. Aborted.")
        return

    success = 0
    failed = []

    for fullname in name_list:
        user = get_user_by_name(fullname)
        if user:
            send_message(sender_uid, user["uid"], message_text)
            success += 1
        else:
            failed.append(fullname)

    print("\n=== BULK MESSAGE REPORT ===")
    print(f"✔ Successfully Sent: {success}")
    if failed:
        print(f"❌ Failed (not found): {', '.join(failed)}")
    print("Done.")
    
    
     
def send_to_single(sender_uid):

    fullname = input("Enter receiver full name: ").strip()
    details = get_user_by_name(fullname)

    if details is None:
        print("\nName not found in database.")
        to_uid = input("Enter receiver UID manually (or 'cancel'): ").strip()
        if to_uid.lower() == "cancel" or to_uid == "":
            print("Cancelled.")
            return
    else:
        to_uid = details["uid"]

    target = get_user_details_by_uid(to_uid)
    if target is None or target.get("role") == "unknown":
        print("The UID you entered does not match any user. Aborting.")
        return

    show_full_user_details(target)

    cont = input("\nDo you want to continue and send the message to this user? (y/n): ").strip().lower()
    if cont != "y":
        print("Aborted by user.")
        return

    message_text = input("Enter message text: ").strip()
    if message_text == "":
        print("Empty message. Aborted.")
        return

    send_message(sender_uid, to_uid, message_text)


def view_inbox(uid):
    df = read_csv_safe(MESSAGES_CSV)
    if df.empty:
        print("\nInbox is empty.")
        return
    inbox = df[df["to_uid"] == uid]
    if inbox.empty:
        print("\nNo messages for you.")
        return

    print(f"\n=== INBOX for {uid} ===")
    for i, row in inbox.iterrows():
        sender = get_user_details_by_uid(str(row["from_uid"]))
        print("\n-------------------------------")
        print(f"From UID : {row['from_uid']}")
        print(f"From Name: {sender.get('name','N/A')}")
        print(f"From Role: {sender.get('role','N/A')}")
        if sender.get("role") == "parent":
            print(f"Parent of Student UID: {sender.get('student_uid','N/A')}")
        if sender.get("role") == "student":
            print(f"Student Class: {sender.get('class','N/A')} | Roll: {sender.get('roll_no','N/A')}")
        if sender.get("role") == "teacher":
            print(f"Teacher Class: {sender.get('class_assigned','N/A')}")
        print(f"Time     : {row['timestamp']}")
        print(f"Message  : {row['message']}")
        print("-------------------------------")

def view_sent(uid):
    df = read_csv_safe(MESSAGES_CSV)
    if df.empty:
        print("\nNo sent messages.")
        return
    sent = df[df["from_uid"] == uid]
    if sent.empty:
        print("\nNo sent messages.")
        return

    print(f"\n=== SENT MESSAGES by {uid} ===")
    for i, row in sent.iterrows():
        target = get_user_details_by_uid(str(row["to_uid"]))
        print("\n-------------------------------")
        print(f"To UID   : {row['to_uid']}")
        print(f"To Name  : {target.get('name','N/A')}")
        print(f"To Role  : {target.get('role','N/A')}")
        print(f"Time     : {row['timestamp']}")
        print(f"Message  : {row['message']}")
        print("-------------------------------")

def parent_menu(parent_uid):
    while True:
        print(f"\n=== Parent Menu ({parent_uid}) ===")
        print("1. Send message")
        print("2. Inbox")
        print("3. Sent")
        print("4. Back")
        c = input("Choose: ").strip()
        if c == "1":
            send_message_full_flow(parent_uid)
        elif c == "2":
            view_inbox(parent_uid)
        elif c == "3":
            view_sent(parent_uid)
        elif c == "4":
            break
        else:
            print("Invalid option.")

def teacher_menu(teacher_uid):
    while True:
        print(f"\n=== Teacher Menu ({teacher_uid}) ===")
        print("1. Send message")
        print("2. Inbox")
        print("3. Sent")
        print("4. Back")
        c = input("Choose: ").strip()
        if c == "1":
            send_message_full_flow(teacher_uid)
        elif c == "2":
            view_inbox(teacher_uid)
        elif c == "3":
            view_sent(teacher_uid)
        elif c == "4":
            break
        else:
            print("Invalid option.")


def messagenow(uid):
    ensure_csv_files()
    df_s = read_csv_safe(STUDENTS_CSV)
    if df_s.empty:
        sample_students = [
            {"uid":"2510A01","name":"Aarist Chauhan","class":"10A","roll_no":"01","password":"stu123","maths":"80","science":"85","english":"78","ss":"72","gujarati":"75","computer":"88","attendance":"95"}
        ]
        pd.concat([df_s, pd.DataFrame(sample_students)], ignore_index=True).to_csv(STUDENTS_CSV, index=False)

    df_p = read_csv_safe(PARENTS_CSV)
    if df_p.empty:
        sample_parents = [
            {"parent_uid":"P01A10","student_uid":"2510A01","parent_name":"Krupa Parmar","password":"par123","phone":"9811199384"}
        ]
        pd.concat([df_p, pd.DataFrame(sample_parents)], ignore_index=True).to_csv(PARENTS_CSV, index=False)

    df_t = read_csv_safe(TEACHERS_CSV)
    if df_t.empty:
        sample_teachers = [
            {"teacher_uid":"2549TK01","name":"Anant Patel","class_assigned":"10A","password":"tch123","phone":"9876500000"}
        ]
        pd.concat([df_t, pd.DataFrame(sample_teachers)], ignore_index=True).to_csv(TEACHERS_CSV, index=False)

   
    if uid.startswith("P") and len(uid) >= 5: 
        parent_menu(uid)
    elif len(uid) == 8 and uid[:4].isdigit() and uid[4:6].isalpha() and uid[6:].isdigit():
        parent_menu(uid)
    else:
        print("This Feature Is Not Available In This Account")


