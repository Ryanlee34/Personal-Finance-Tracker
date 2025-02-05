from finance_manager import FinanceManager


def display_menu():
    """
    Display the main menu options and prompt the user for a choice.

    Returns:
        str: The chosen menu option.
    """
    print("\n=== Personal Finance Manager ===")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View Transactions by Type")
    print("4. Exit")
    return input("Choose an option (1-4): ").strip()


def main():
    """
    Main function to run the finance manager program.
    Allows users to add, view, and filter transactions.
    """
    manager = FinanceManager()

    while True:
        choice = display_menu()
        if choice == "1":
            manager.add_transaction()
        elif choice == "2":
            manager.view_transactions()
        elif choice == "3":
            manager.view_transactions_by_type()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()



