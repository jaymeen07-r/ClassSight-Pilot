def librarian_dashboard():
    print("\n=== LIBRARIAN DASHBOARD ===")
    print("1. Book Issue / Return")
    print("2. Track Library Usage")
    print("3. Student Reading Analytics")
    print("4. Add / Remove Books")
    print("5. Fine Management")
    print("6. Generate Library Reports")
    print("0. Logout")

    choice = input("Choose an option:  ").strip()
    
    if choice == "0":
        print("Logged out.")
        return
    else:
        print("Feature coming soon!")
        librarian_dashboard()