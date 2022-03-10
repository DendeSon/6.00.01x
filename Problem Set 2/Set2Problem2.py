"""
Objective: Find a minimum fixed monthly payment needed to pay off credit card
within 12 months. Uses multiples of $10.
'balance' and 'annualInterestRate' are given by the grader.
Prints out the lowest fixed monthly payment rate, rounded to 2 decimals.
"""

monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)