from models.teachers import *
from core.detect_csv_files import *

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