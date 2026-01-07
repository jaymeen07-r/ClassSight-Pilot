def it_admin_dashboard():
    print("\n=== IT ADMIN DASHBOARD ===")
    print("1. System Configuration")
    print("2. Security Settings")
    print("3. API Integrations")
    print("4. User Access Management")
    print("5. Network Monitoring")
    print("6. Log Viewer / Debug Tools")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        it_admin_dashboard()