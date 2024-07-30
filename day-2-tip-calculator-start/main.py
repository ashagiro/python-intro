print("welcome to the tip calculator!")
print("what was the total bill?")
total_bills = input()
print("how much tip would you like to give? 10, 12, or 15?")
tip_amount = input()
print("how many people to split the bill?")
split_amount = input()
tip_percent = int(tip_amount) / 100 + 1
paying_amount = (float(total_bills) / int(split_amount)) * tip_percent
paying_amount = "{:.2f}".format(paying_amount)
print(f"each person should pay {paying_amount}")