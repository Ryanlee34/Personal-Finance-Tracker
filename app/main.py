from finance_manager import FinanceManager
import visualizations

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
    print("4. Generate Income Pie Chart")
    print("5. Generate Expense Pie Chart")
    print("6. Generate Income vs. Expense Line Chart")
    print("7. Exit")
    return input("Choose an option (1-7): ").strip()

def main():
    """Main function to run the finance manager program."""
    manager = FinanceManager()

    while True:
        choice = display_menu()
        if choice == "1":
            manager.add_transaction()
            print("\nFetching updated transactions after adding new entry...")
            manager.view_transactions()
        elif choice == "2":
            print("\nFetching fresh transactions...")
            manager.view_transactions()
        elif choice == "3":
            print("\nFetching transactions by type...")
            manager.view_transactions_by_type()
        elif choice == "4":
            print("\nGenerating Income Pie Chart...")
            visualizations.pie_chart("Income")
        elif choice == "5":
            print("\nGenerating Expense Pie Chart...")
            visualizations.pie_chart("Expense")
        elif choice == "6":
            print("\nGenerating Income vs. Expense Line Chart...")
            visualizations.line_chart()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()

