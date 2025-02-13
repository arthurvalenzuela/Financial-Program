import numpy as np
import os
import matplotlib.pyplot as plt  ## For visualization


class BudgetManager:
    ## A class to manage income, expenses, and savings
    def __init__(self):
        self.income = []
        self.expenses = []
        self.savings_goal = 0

    def add_income(self, amount):
        ## Add income to the income list
        if amount > 0:
            self.income.append(amount)
        else:
            raise ValueError("Income must be a positive value.")

    def add_expense(self, amount):
        ## Add expense to the expenses list
        if amount > 0:
            self.expenses.append(amount)
        else:
            raise ValueError("Expense must be a positive value.")

    def set_savings_goal(self, goal):
        ## Set the savings goal
        if goal >= 0:
            self.savings_goal = goal
        else:
            raise ValueError("Savings goal must be non-negative.")

    def calculate_summary(self):
        ## Calculate total income, total expenses, and income after expenses
        total_income = np.sum(self.income) if self.income else 0
        total_expenses = np.sum(self.expenses) if self.expenses else 0
        income_after_expenses = total_income - total_expenses
        return total_income, total_expenses, income_after_expenses


class PeriodicBudget(BudgetManager):
    ## A subclass to handle periodic budgets (monthly or weekly)
    def __init__(self, period="monthly"):
        super().__init__()
        self.period = period


def display_menu():
    ## Display the main menu options
    print("\n--- Budget Manager ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Set Savings Goal")
    print("4. Calculate Summary")
    print("5. Visualize Budget")
    print("6. Save Period")
    print("7. Load Data")
    print("8. Quit")


def save_summary_to_file(filename, summary):
    ## Save the budget summary to a text file
    try:
        with open(filename, 'w') as file:
            file.write(summary)
        print(f"Summary saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def save_period_to_file(filename, budget):
    ## Save the budget summary to a text file without the period
    try:
        total_income, total_expenses, income_after_expenses = budget.calculate_summary()
        period_summary = (
            f"--- Budget Summary ---\n"
            f"Total Income: ${total_income:.2f}\n"
            f"Total Expenses: ${total_expenses:.2f}\n"
            f"Income After Expenses: ${income_after_expenses:.2f}\n"
            f"Savings Goal: ${budget.savings_goal:.2f}\n"
        )
        with open(filename, 'w') as file:
            file.write(period_summary)
        print(f"Summary saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def load_data_from_file(filename, budget):
    ## Load budget data from a file
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            budget.income = []
            budget.expenses = []
            for line in lines:
                if line.startswith("Income:"):
                    budget.income.append(float(line.split(":")[1].strip()))
                elif line.startswith("Expense:"):
                    budget.expenses.append(float(line.split(":")[1].strip()))
                elif line.startswith("Savings Goal:"):
                    budget.savings_goal = float(line.split(":")[1].strip())
        print(f"Data loaded from {filename}")
    except Exception as e:
        print(f"Error loading file: {e}")


def visualize_budget(budget):
    ## Visualize the budget using a bar chart
    total_income, total_expenses, income_after_expenses = budget.calculate_summary()
    labels = ['Income', 'Expenses', 'Income After Expenses']
    values = [total_income, total_expenses, income_after_expenses]
    
    # Create the bar chart
    plt.bar(labels, values, color=['green', 'red', 'blue'])
    plt.title("Budget Overview")
    plt.ylabel("Amount ($)")
    
    # Display the graph
    print("\nDisplaying the budget visualization. Close the graph window to continue.")
    plt.show(block=False)  # Non-blocking display
    plt.pause(5)  # Keep the graph open for 5 seconds (optional)
    plt.close()   # Close the graph window automatically

def main():
    ## Create an instance of PeriodicBudget
    budget = PeriodicBudget(period="monthly")

    while True:
        ## Display menu
        display_menu()

        ## Get user choice
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        ## Handle user choices
        if choice == 1:
            try:
                amount = float(input("Enter income amount: "))
                budget.add_income(amount)
                print(f"Income of {amount} added successfully.")
            except ValueError as e:
                print(e)

        elif choice == 2:
            try:
                amount = float(input("Enter expense amount: "))
                budget.add_expense(amount)
                print(f"Expense of {amount} added successfully.")
            except ValueError as e:
                print(e)

        elif choice == 3:
            try:
                goal = float(input("Enter savings goal: "))
                budget.set_savings_goal(goal)
                print(f"Savings goal set to {goal}.")
            except ValueError as e:
                print(e)

        elif choice == 4:
            ## Calculate and display the summary
            total_income, total_expenses, income_after_expenses = budget.calculate_summary()
            summary = (
                f"--- Budget Summary ---\n"
                f"Total Income: ${total_income:.2f}\n"
                f"Total Expenses: ${total_expenses:.2f}\n"
                f"Income After Expenses: ${income_after_expenses:.2f}\n"
                f"Savings Goal: ${budget.savings_goal:.2f}\n"
            )
            print(summary)

        elif choice == 5:
            visualize_budget(budget)

        elif choice == 6:
            ## Save the budget summary to a file
            filename = "budget_period.txt"
            save_period_to_file(filename, budget)

        elif choice == 7:
            ## Load budget data from a file
            filename = input("Enter the filename to load data from: ")
            load_data_from_file(filename, budget)

        elif choice == 8:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
