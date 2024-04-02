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

def fetch_data():
    need_to_fetch_balance = True
    need_to_fetch_interest = True
    need_to_fetch_maturity = True
    balance = 0.0
    interest = 0.0
    maturity = 0
    while need_to_fetch_balance:
        balance_input = input("Please enter your initial balance: ")
        if is_float(balance_input):
            balance = float(balance_input)
            need_to_fetch_balance = False
        else:
            print_invalid()
    while need_to_fetch_interest:
        interest_input = input("Next, please enter your interest rate: ")
        if is_float(interest_input):
            interest = float(interest_input)
            need_to_fetch_interest = False
        else:
            print_invalid()
    while need_to_fetch_maturity:
        maturity_input = input("Finally, please enter term length (in months): ")
        if maturity_input.isdigit():
            maturity = int(maturity_input)
            need_to_fetch_maturity = False
        else:
            print_invalid()
    
    return {
        'balance': balance,
        'interest': interest,
        'maturity': maturity
    }

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Welcome to DIY Bank, thank you for your business!")
    print("To get started we will need to gather data about your savings account -")
    savings = fetch_data()

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings["balance"], savings["interest"], savings["maturity"])

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Over the term of {savings['maturity']} months")
    print(f"your savings will have earned ${interest_earned: ,.2f}.")
    print(f"for a total of ${updated_savings_balance: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("Now we will need to gather data about your CD account -")
    cd = fetch_data()

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd["balance"], cd["interest"], cd["maturity"])
    
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Over the term of {cd['maturity']} months")
    print(f"your CD will have earned ${interest_earned: ,.2f}.")
    print(f"for a total of ${updated_cd_balance: ,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()