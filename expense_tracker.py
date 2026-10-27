
import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    description = input("Enter expense description: ")

    try:
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for row in expenses:
        print(f"Description: {row[0]}, Amount: Rs. {float(row[1]):.2f}")


def total_expenses():
    total = 0

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

    print(f"\nTotal Expenses: Rs. {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
