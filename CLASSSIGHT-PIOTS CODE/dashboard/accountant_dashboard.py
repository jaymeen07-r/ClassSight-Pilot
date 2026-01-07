def accountant_dashboard():
    print("\n=== ACCOUNTANT / FEE MANAGER DASHBOARD ===")
    print("1. Fee Tracking")
    print("2. Payment History")
    print("3. Salary Statements")
    print("4. Financial Reports")
    print("5. Manage Discounts / Scholarships")
    print("6. Auto-Generate Fee Receipts")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()

    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        accountant_dashboard()