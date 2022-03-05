money_start = input("Please enter the money you started with: ")

saving_years = input("Please enter the number of years you have saved: ")

interest_rate = input("Please enter the interest rate as a number: ")

money_result = int(money_start) * float(interest_rate) * int(saving_years)

print(money_result)

print(money_result > 10000)



