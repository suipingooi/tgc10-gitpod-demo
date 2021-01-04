amount_loaned = float(input("how much did you borrow? "))
interest_rate = float(input("monthly interest rate? "))
repayment_per_month = float(input("monthly repayment "))

# a state variable to represent how many months it will take to repay
months_needed_to_repay = 0
while amount_loaned >= 0:
    interest_for_this_month = interest_rate/100 * amount_loaned
    amount_loaned += interest_for_this_month
    print("amount still owe ", amount_loaned)
    amount_loaned -= repayment_per_month
    months_needed_to_repay += 1

print("months needed for repayment = ", months_needed_to_repay)
