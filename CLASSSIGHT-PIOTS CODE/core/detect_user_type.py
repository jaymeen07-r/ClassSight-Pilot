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