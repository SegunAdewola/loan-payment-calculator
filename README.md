# Loan Payment Calculator

## Description
This Python program calculates the monthly payment required to pay off a loan within a specified number of months, given the loan amount and monthly interest rate. The program uses input validation to ensure valid values for the interest rate, loan amount, and repayment period.

## Features
- **Monthly Payment Calculation**: Calculates monthly payments based on the loan amount, interest rate, and repayment term.
- **Input Validation**: Ensures that the user inputs positive values for all parameters.
- **Loan Summary**: Displays the loan amount, interest rate, repayment months, and calculated monthly payment.

## Usage

1. Clone or download the script.
2. Run the script from the terminal or command line:

   ```bash
   python loan_payment_calculator.py
   ```
3. Follow the prompts to input:
    - Monthly interest rate (as a decimal).
    - Loan amount.
    - Number of months to repay the loan.
### Example
```plaintext
Enter the monthly interest rate as a percentage (e.g., 2.5% = 0.025): 0.025
Enter the loan amount: 10000
Enter the number of months to repay the loan: 24

Loan Summary:
Loan Amount: $10,000.00
Interest Rate: 2.50%
Payment Months: 24
Monthly Payment: $440.11
```

## Functions
- **`calc_monthly_payment(interest_rate, loan_amount, months)`**: Calculates the monthly payment required to pay off the loan.
    - **Arguments**:
        - **`interest_rate (float)`**: Monthly interest rate as a decimal.
        - **`loan_amount (float)`**: Amount of the loan.
        - **`months (float)`**: Number of months for repayment.
    - **Returns**: The calculated monthly payment.
- **`main()`**: Prompts the user for inputs, performs validation, and displays the loan summary.

## Requirements
- **Python 3.x**

## License
This project is licensed under the MIT License.