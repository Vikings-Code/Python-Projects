# prompt user for principal amount, interest rate, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a decimal): "))
time = float(input("Enter the time period in years: "))

# calculate the simple interest
interest = principal * rate * time

# calculate the total amount after simple interest
total_amount = principal + interest

# print the result
print("The simple interest is: ${:.2f}".format(interest))
print("The total amount after simple interest is: ${:.2f}".format(total_amount))

