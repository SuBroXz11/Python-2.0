print('Welcome to the Tip Calculator.')
print('---------------------------')

# Ask the user for the total bill
total_bill = float(input('What was the total bill? $'))

# Ask the user how many people to split the bill
bill_split = int(input('How many people to split the bill? '))

# Ask the percentage tip you would like to give: 10, 12, or 15
tip_percent = float(input('What percentage tip would you like to give? 10, 12, or 15? '))

# Calculate the total amount including the tip
total_with_tip = total_bill + (total_bill * tip_percent / 100)

# Calculate per person payment
single_person_pay = total_with_tip / bill_split

# Format the result to 2 decimal places
formatted_payment = "{:.2f}".format(single_person_pay)

# End result
print(f'Each person should pay: ${formatted_payment}')
