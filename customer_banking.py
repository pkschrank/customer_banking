# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def print_invalid():
    """A simple function to let the user know the value entered is invalid"""
    print("Invalid value, please try again")

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Welcome to DIY Bank, thank you for your business!")
    print("To get started we will need to gather data about your savings account -")
    need_to_fetch_savings_balance = True
    need_to_fetch_savings_interest = True
    need_to_fetch_savings_maturity = True
    savings_balance = 0.0
    savings_interest = 0.0
    savings_maturity = 0
    while need_to_fetch_savings_balance:
        savings_balance_input = input("Please enter your initial balance: ")
        if is_float(savings_balance_input):
            savings_balance = float(savings_balance_input)
            need_to_fetch_savings_balance = False
        else:
            print_invalid()
    while need_to_fetch_savings_interest:
        savings_interest_input = input("Now, please enter your interest rate: ")
        if is_float(savings_interest_input):
            savings_interest = float(savings_interest_input)
            need_to_fetch_savings_interest = False
        else:
            print_invalid()
    while need_to_fetch_savings_maturity:
        savings_maturity_input = input("Finally, please enter term length (in months): ")
        if savings_maturity_input.isdigit():
            savings_maturity = int(savings_maturity_input)
            need_to_fetch_savings_maturity = False
        else:
            print_invalid()

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Over the term of {savings_maturity} months")
    print(f"your savings will have earned ${interest_earned: ,.2f}.")
    print(f"for a total of ${updated_savings_balance: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    need_to_fetch_cd_balance = True
    need_to_fetch_cd_interest = True
    need_to_fetch_cd_maturity = True
    cd_balance = 0.0
    cd_interest = 0.0
    cd_maturity = 0
    while need_to_fetch_cd_balance:
        cd_balance_input = input("Please enter your initial balance: ")
        if is_float(cd_balance_input):
            cd_balance = float(cd_balance_input)
            need_to_fetch_cd_balance = False
        else:
            print_invalid()
    while need_to_fetch_cd_interest:
        cd_interest_input = input("Now, please enter your interest rate: ")
        if is_float(cd_interest_input):
            cd_interest = float(cd_interest_input)
            need_to_fetch_cd_interest = False
        else:
            print_invalid()
    while need_to_fetch_cd_maturity:
        cd_maturity_input = input("Finally, please enter term length (in months): ")
        if cd_maturity_input.isdigit():
            cd_maturity = int(cd_maturity_input)
            need_to_fetch_cd_maturity = False
        else:
            print_invalid()

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Over the term of {cd_maturity} months")
    print(f"your CD will have earned ${interest_earned: ,.2f}.")
    print(f"for a total of ${updated_cd_balance: ,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()