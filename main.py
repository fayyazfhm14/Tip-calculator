# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))

# Mathematics code 
tip_decimal = (tip_percentage) / 100
total_bill = bill / split_bill * (1 + tip_decimal)
total_bill_rounded = round(total_bill, 2)
total_bill_rounded = "{:.2f}".format(total_bill)

# output
print(f"Each person should pay: ${total_bill_rounded}")