def exam_coordinator_dashboard():
    print("\n=== EXAM COORDINATOR DASHBOARD ===")
    print("1. Create Exam Timetables")
    print("2. Manage Marksheets")
    print("3. AI-Based Result Analysis")
    print("4. Approve Results")
    print("5. Generate Reports & Certificates")
    print("6. Student Performance Comparison")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        exam_coordinator_dashboard()
