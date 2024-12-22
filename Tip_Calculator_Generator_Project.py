#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome To Tip Calculator!")
Bill = float(input("Enter The Total Amount:\n"))
Tip_Percentage = int(input("How Much You Want To Tip (10%, 12%, 15%, 20%):\n"))
people = int(input("How Many People are Present To Split The Bill:\n"))

#Calculations:
Tip_Amount = (Bill * Tip_Percentage) / 100
Total_Bill_Amount = Bill + Tip_Amount
Bill_per_person = Total_Bill_Amount / people
Final_Amount = round(Bill_per_person,2)

# If you want the final_amount to always have 2 decimal places.
Final_Amount = "{:.2f}".format(Bill_per_person)
print(f"Each Person Should Pay: {Final_Amount}")
