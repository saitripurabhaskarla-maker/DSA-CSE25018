# Recursive function to calculate p^n (power)
def power(p, n):
    # Base case: anything raised to power 0 is 1
    if n == 0:
        return 1
    # Recursive case: p^n = p * p^(n-1)
    else:
        return p * power(p, n - 1)


# Main program to calculate Compound Interest
def compound_interest():
    principal = float(input("Enter the Principal amount: "))
    rate = float(input("Enter the Rate of Interest (in %): "))
    years = int(input("Enter the Number of Years: "))

    # Growth factor per year = (1 + rate/100)
    growth_factor = 1 + (rate / 100)

    # Using recursion to calculate (growth_factor)^years
    final_amount = principal * power(growth_factor, years)

    compound_interest_earned = final_amount - principal

    print(f"Final Amount after {years} years: {final_amount:.2f}")
    print(f"Compound Interest Earned: {compound_interest_earned:.2f}")


# Run the program
compound_interest()
