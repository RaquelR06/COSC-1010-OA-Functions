# Programming Assignment 5: Automobile Costs
# COSC 1010

def get_monthly_cost(expense_name):
    """Prompts the user to enter a monthly cost for a specific expense."""
    cost = float(input(f"Enter the monthly cost for {expense_name}: $"))
    return cost

def calculate_totals(loan, insurance, gas, oil, tires, maintenance):
    """Calculates the monthly and annual automobile expenses."""
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    total_annual = total_monthly * 12
    return total_monthly, total_annual

def display_results(total_monthly, total_annual):
    """Displays the formatted cost summary."""
    print("\n--- Automobile Expense Summary ---")
    print(f"Total Monthly Cost: ${total_monthly:,.2f}")
    print(f"Total Annual Cost:  ${total_annual:,.2f}")

def main():
    print("Please enter your monthly automobile expenses below:\n")
    
    # Collect monthly costs
    loan = get_monthly_cost("Loan Payment")
    insurance = get_monthly_cost("Insurance")
    gas = get_monthly_cost("Gas")
    oil = get_monthly_cost("Oil")
    tires = get_monthly_cost("Tires")
    maintenance = get_monthly_cost("Maintenance")
    
    # Calculate costs
    total_monthly, total_annual = calculate_totals(loan, insurance, gas, oil, tires, maintenance)
    
    # Output total expenses
    display_results(total_monthly, total_annual)

# Call the main function to run the program
if __name__ == "__main__":
    main()
    
