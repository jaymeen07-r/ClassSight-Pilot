def super_admin_dashboard():
    print("\n=== SUPER ADMIN DASHBOARD ===")
    print("1. Manage All Institutes")
    print("2. Manage All Users (Admins/Teachers/Students)")
    print("3. System Analytics")
    print("4. Approve High-Level Reports")
    print("5. Broadcast System Notices")
    print("6. Global Settings & Configurations")
    print("7. Data Backup & Restore")
    print("8. API / Integrations")
    print("0. Logout")

    choice = input("Choose: ").strip()
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        super_admin_dashboard()