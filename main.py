import data_handler as data
import Validators as Valid
import visualizations as vis

# Function to display the main menu options
def display_menu():
    # Print menu options for user interaction
    print("\n=== Personal Finance Manager ===")
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. Filter Transactions")
    print("4. Income/Expense Pie Chart")
    print("5. Line Chart (Income vs Expense)")
    print("6. Exit")
    return input("Choose an option (1-6): ").strip()  # Get user's choice


# Main entry point for the program
def main():
    # Dictionary linking input fields to their validation functions
    functions = {
        "Date": Valid.get_valid_date,
        "Transaction Type": Valid.get_transaction_type,
        "Category": Valid.get_category,
        "Income Type": Valid.get_income_type,
        "Amount": Valid.get_amount,
        "Details": Valid.get_description
    }

    while True:
        # Show the menu and get user input
        menu_choice = display_menu()

        # Validate menu input
        if menu_choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid Input, Please Try again")
            continue

        try:
            # Add a new transaction
            if menu_choice == "1":
                data.data_processor(functions)

            # View all transactions
            elif menu_choice == "2":
                data.data_output()

            # Filter and view specific transactions
            elif menu_choice == "3":
                data.data_select()

            # Generate a pie chart (income or expense distribution)
            elif menu_choice == "4":
                e_or_i = input("1. Expense Chart\n2. Income Chart\nChoose an option (1-2): ").strip()
                if e_or_i in ["1", "2"]:
                    vis.pie_chart(e_or_i)
                else:
                    print("Invalid input. Please try again.")

            # Generate a line chart (income vs expense over time)
            elif menu_choice == "5":
                vis.line_chart()

            # Exit the program
            elif menu_choice == "6":
                print("Thank you for using the Personal Finance Manager. Goodbye!")
                break

        # Catch and handle any unexpected errors
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for user input before returning to the menu
        input("\nPress Enter to return to the menu.")


# Run the program only when executed directly
if __name__ == "__main__":
    main()


