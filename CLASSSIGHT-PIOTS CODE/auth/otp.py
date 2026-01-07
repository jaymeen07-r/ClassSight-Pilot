import random

def generate_otp():
    return str(random.randint(100000,999999))


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