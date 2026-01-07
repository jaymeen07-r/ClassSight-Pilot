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