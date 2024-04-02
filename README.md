# customer_banking

# Interest Calculation on different account types

The customer banking module will handle basic calculations on a given account. It will support general savings and CD accounts and report back on the total account balance at the end of a term along with the amount of interest earned.

## Workflow
- User is greeted by the application and is then prompted to enter the 3 points of criteria for calculating against a savings account. Each value will be type checked. If it is not a valid numeric type, the user will be notified and prompted to try again.
    1. initial balance
    2. interest rate
    3. term length (in months)
- The user is presented with the new balance and the total interest earned in their savings account.
- The user is then prompted for the same criteria but for a CD account. If it is not a valid numeric type, the user will be notified and prompted to try again.
    1. initial balance
    2. interest rate
    3. term length (in months)
- The user is presented with the new balance and the total interest earned in their CD account.