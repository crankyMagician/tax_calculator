def calculate_taxes(annual_salary, months_worked, write_offs):
    # Constants
    SOCIAL_SECURITY_RATE = 0.062
    MEDICARE_RATE = 0.0145
    PA_STATE_TAX_RATE = 0.0307
    PHILADELPHIA_WAGE_TAX_RATE = 0.0379

    # Calculate annualized income
    monthly_salary = annual_salary / 12
    total_income = monthly_salary * months_worked

    # Adjusted taxable income
    adjusted_income = total_income - write_offs

    # Federal Income Tax Calculation
    def calculate_federal_tax(income):
        if income <= 11000:
            return income * 0.1
        elif income <= 44725:
            return 1100 + (income - 11000) * 0.12
        elif income <= 95375:
            return 5147 + (income - 44725) * 0.22
        elif income <= 182100:
            return 16290 + (income - 95375) * 0.24
        elif income <= 231250:
            return 37104 + (income - 182100) * 0.32
        elif income <= 578125:
            return 52832 + (income - 231250) * 0.35
        else:
            return 174238 + (income - 578125) * 0.37

    federal_tax = calculate_federal_tax(adjusted_income)

    # State and Local Taxes
    state_tax = adjusted_income * PA_STATE_TAX_RATE
    local_tax = adjusted_income * PHILADELPHIA_WAGE_TAX_RATE

    # Social Security and Medicare Taxes
    social_security_tax = total_income * SOCIAL_SECURITY_RATE
    medicare_tax = total_income * MEDICARE_RATE

    # Total Taxes
    total_taxes = federal_tax + state_tax + local_tax + social_security_tax + medicare_tax

    # Remaining Paychecks
    total_paychecks = 26  # Total paychecks in a year assuming bi-weekly pay
    remaining_paychecks = total_paychecks - (months_worked / 12 * total_paychecks)

    # Ensure remaining_paychecks is not zero to avoid division by zero
    if remaining_paychecks == 0:
        remaining_paychecks = 1

    # Savings per remaining paycheck
    paid_taxes = total_taxes / 12 * months_worked
    remaining_taxes = total_taxes - paid_taxes
    savings_per_paycheck = remaining_taxes / remaining_paychecks

    return total_taxes, savings_per_paycheck


def main():
    # User inputs
    annual_salary = float(input("Enter your annual salary: "))
    months_worked = int(input("Enter the number of months you've worked this year: "))
    write_offs = float(input("Enter your tax write-offs: "))

    # Calculate taxes and savings
    total_taxes, savings_per_paycheck = calculate_taxes(annual_salary, months_worked, write_offs)

    # Output results
    print(f"\nTotal estimated taxes for the year: ${total_taxes:,.2f}")
    print(f"Amount to save from each remaining paycheck: ${savings_per_paycheck:,.2f}")


if __name__ == "__main__":
    main()
