# Program to calculate sales commission

# Input: Sales amount from user
sales = float(input("Enter total sales amount (₹): "))

# Define commission rules
if sales >= 100000:
    commission_rate = 0.10  # 10%
elif sales >= 50000:
    commission_rate = 0.07  # 7%
elif sales >= 20000:
    commission_rate = 0.05  # 5%
else:
    commission_rate = 0.02  # 2%

# Calculate commission
commission = sales * commission_rate

# Output
print(f"Commission Rate: {commission_rate * 100}%")
print(f"Total Commission: ₹{commission}")
