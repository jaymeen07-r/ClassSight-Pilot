from core.detect_csv_files import *

def send_message_teacher_to_parent():
    from_uid = input("Enter your Teacher UID: ").strip()
    to_uid = input("Enter Parent UID: ").strip()
    message = input("Enter Message: ").strip()
    df = pd.read_csv(MESSAGES_CSV)
    df.loc[len(df)] = [from_uid,to_uid,message,datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    df.to_csv(MESSAGES_CSV,index=False)
    print("Message sent successfully.")