# Financial Planner

The Financial Planner is a Python program designed to help individuals and businesses calculate their projected monthly savings by inputting their income and expenses. This tool provides a simple way to track finances, set savings goals, and generate a budget summary.

## Table of Contents
1. [Description](#description)
2. [Objective](#objective)
3. [Features](#features)
4. [How to Use](#how-to-use)
5. [Limitations](#limitations)
6. [Future Enhancements](#future-enhancements)
7. [Installation](#installation)
8. [Contributing](#contributing)
9. [License](#license)
10. [Credits](#credits)

## Description
In our financial program my teammate and I are looking to solve problems such as companies, business owners and individuals who are not sure how to calculate their projected monthly savings that works for them by inputting their monthly income and expenses. The solutions that we are implementing in our financial tracking program are expense categorization, the ability to set financial goals and cash flow monitoring. 

## Objective
Our programs objectives are to monitor cash flow analysis, income tracking and the ability to set financial goals such as a monthly budget and savings based on the user’s income and expenses each month.

## Limitations
Some limitations of the program would be the reliance of the user input being that they choose the option first then press enter and then input the amount, as well as the user using “,”. Some recommendation on improving these limitations of the program regarding the reliance on user input accuracy, because the program will only read # inputs without “,” for example, instead of user inputting “1,000” user must input “1000”. 

## Future Enhancements
Future enhancements would include : Making the program easier to run, making the option of using commas "," when inputing an amount (ex 1,00). More options for chart visualizations.  

# Installation

## Clone the repository

```bash
git clone https://github.com/arthurvalenzuela/Financial-Program.git
```
1. Navigate to project directory
```bash
cd Financial-Program
```
2. Run the program
```bash
python FinancialPlanner.py
```
## Features
- Income Tracking: Input your monthly income.
- Expense Tracking: Add your monthly expenses.
- Savings Goals: Set a savings goal and calculate remaining savings.
- Budget Summary: Generate a detailed summary of income, expenses, savings goals, and remaining savings.
- File Output: Save the budget summary to a .txt file for future reference.

## Contributing

We welcome contributions to improve the Financial Planner! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
3. Commit changes
   ```bash
   git commit -m "Add your feature"
4. Push to the branch
   ```bash
   git push origin feature/your-feature-name
5. Open a pull request
   
## How to Use
Navigate to the project directory where the program is located 

```bash
cd Financial-Program
```
Run the program using the command:
```bash
python FinancialPlanner.py
```
1. Input Monthly Income :
When prompted, enter your total monthly income as a number (e.g., 5000).
Do not include commas or special characters (e.g., input 5000 instead of 5,000).
2. Add Monthly Expenses :
Enter your monthly expenses one by one when prompted.
For example, you can add expenses like rent, utilities, groceries, etc., as numbers (e.g., 1500 for rent).
3. Set a Savings Goal :
Input your desired savings goal for the month (e.g., 1000).
This will help the program calculate how much you need to save based on your income and expenses.
4. View the Budget Summary :
After entering your income, expenses, and savings goal, the program will generate a budget summary.
5. The summary includes:
Total Income
Total Expenses
Remaining Savings
Savings Goal
6. Save the Summary :
The program will save the budget summary to a .txt file for future reference.
You can find the saved file in the project directory.
7. Quit the Program :
Once you’re done, choose the "Quit" option to exit the program.
You can rerun the program later to track additional financial data.
8. Example 
```bash
--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 1
Enter income amount: 5000
Income of 5000 added successfully.

--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 2
Enter expense amount: 1500
Expense of 1500 added successfully.

--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 3
Enter savings goal: 1000
Savings goal set to 1000.

--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 4
--- Budget Summary ---
Total Income: $5000.00
Total Expenses: $1500.00
Remaining Savings: $3500.00
Savings Goal: $1000.00

--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 5
Summary saved to budget_summary.txt

--- Budget Manager ---
1. Add Income
2. Add Expense
3. Set Savings Goal
4. Calculate Summary
5. Save Summary to File
6. Quit
Enter your choice (1-6): 6
Exiting the program. Goodbye!
```
Tips for Users
- Avoid Commas : When entering numbers, do not use commas (e.g., input 5000 instead of 5,000).
- Follow Prompts Carefully : Ensure you select the correct menu option and provide valid inputs to avoid errors.
- Save Your Data : Always save the budget summary to a file so you can refer to it later.

## Credits

This project was developed as a team effort by:

- **Alissia Ornelas** 
- **Jesus Valenzuela**

## Licence

MIT License

Copyright (c) 2025 Arthur Valenzuela and Alissia Ornelas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
