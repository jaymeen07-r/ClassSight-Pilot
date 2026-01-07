import datetime
import random
from core.detect_csv_files import *

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
