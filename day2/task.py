print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_with_percentage = tip/100
tip_with_bill = tip_with_percentage*bill
total_bill = tip_with_bill+bill
bill_person = total_bill / people
final_amount = round(bill_person,2)
print("Each person should pay: $",final_amount)
