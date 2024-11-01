# Defining a function to calculate the monthly payment amount
def calc_monthly_payment(interest_rate, loan_amount, months):
    """
    Calculates the monthly payment required to pay off a loan within a specific number of months.

    Args:
        interest_rate (float): The monthly interest rate as a decimal.
        loan_amount (float): The amount of the loan.
        months (float): The number of months to repay the loan.

    Returns:
        float: The monthly payment amount.
    """
    monthly_payment = 0  # Declare local monthly payment variable
    
    # Applying the loan payment formula
    monthly_payment = (interest_rate * loan_amount) / (1 - (1 + interest_rate) ** -months)
    
    return monthly_payment

# Defining the main function
def main():
    """
    The main function that prompts the user for the loan amount, interest rate, and number of months,
    and displays the calculated monthly payment.
    """
    interest_rate = 0.0  # Declare local interest rate variable
    loan_amount = 0.0  # Declare local loan amount variable
    months = 0  # Declare local months variable
    monthly_payment = 0.0  # Declare local monthly payment variable
    
    # Prompting the user for input with validation using the walrus operator
    while (interest_rate := float(input("Enter the monthly interest rate as a percentage (e.g., 2.5% = 0.025): "))) <= 0:
        print("Interest rate must be greater than 0. Try again.")
    
    while (loan_amount := float(input("Enter the loan amount: "))) <= 0:
        print("Loan amount must be greater than 0. Try again.")
    
    while (months := int(input("Enter the number of months to repay the loan: "))) <= 0:
        print("Number of months must be greater than 0. Try again.")
    
    # Calculate the monthly payment using the function
    monthly_payment = calc_monthly_payment(interest_rate, loan_amount, months)
    
    # Display the results
    print("\nLoan Summary:")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Interest Rate: {interest_rate * 100:.2f}%")
    print(f"Payment Months: {months}")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")

# Calling the main function
if __name__ == "__main__":
    main()