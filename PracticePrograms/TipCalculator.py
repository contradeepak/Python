bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip = (bill_amount * tip_percentage) / 100
total = bill_amount + tip
print(f"Tip: {tip}")
print(f"Total amount to be paid: {total}")