# Get user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to be saved, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Constants
portion_down_payment = 0.25  # 25% down payment
current_savings = 0  # Starting savings
r = 0.04  # Annual investment return

# Calculate the down payment required
down_payment = total_cost * portion_down_payment

# Calculate the monthly savings amount
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved

# Calculate the number of months required to save up for the down payment
num_months = 0
while current_savings < down_payment:
    current_savings += monthly_savings  # Add monthly savings
    current_savings += current_savings * r / 12  # Add investment returns
    num_months += 1

# Print the result
print("Number of months:", num_months)