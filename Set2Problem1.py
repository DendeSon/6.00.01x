"""
Objective: Find your credit card balance after 1 year if only paying the 
minimum monthly payment.
'balance', 'annualInterestRate' and 'monthlyPaymentRate' are given by grader.
Prints out the remaining balance after 1 year, rounded to 2 decimals.
"""

month = 0
previousBalance = balance
newBalance = 0

monthlyInterestRate = annualInterestRate/12.0

#First Month
if month == 0:
    minMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaid = previousBalance - minMonthlyPayment
    monthlyBalanceUpdated = monthlyUnpaid + (monthlyInterestRate * monthlyUnpaid)
    previousBalance = monthlyBalanceUpdated
    month += 1

while (month > 0) and (month < 12):
    minMonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaid = previousBalance - minMonthlyPayment
    monthlyBalanceUpdated = monthlyUnpaid + (monthlyInterestRate * monthlyUnpaid)
    previousBalance = monthlyBalanceUpdated
    #newBalance = monthlyBalanceUpdated
    #previousBalance = newBalance
    month += 1
  
print("Remaining balance: " + str(round(previousBalance, 2)))