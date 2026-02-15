from database import create_table, add_expense, get_all_expenses
import analytics

def view_expenses():
    rows = get_all_expenses()
    if not rows:
        print("No expenses found.")
    else:
        for row in rows:
            print(row)


def main():
    create_table()

    while True:
        print("\n====== PERSONAL EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Show Bar Chart")
        print("6. Show Pie Chart")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            category = input("Category: ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            add_expense(category, amount, description)
            print("Expense added successfully!")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            analytics.monthly_summary()

        elif choice == "4":
            analytics.category_summary()

        elif choice == "5":
            analytics.show_bar_chart()

        elif choice == "6":
            analytics.show_pie_chart()

        elif choice == "7":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
