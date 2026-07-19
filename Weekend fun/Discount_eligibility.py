# name: Discount_eligibility
# read total_bill and is_member ("yes" or "no")
# if total_bill >= 1000 and is_member == "yes" -> 10% off
# final amount = total bill - (total_bill * 10 / 100) 
# print final amount
# if total_bill >= 1000 but not member -> 5% off
# final amount = total_bill - (total_bill * 5 / 100)
# print final amount 
# else No discount total_bill final amount

total_bill = float( input("Enter the total bill:"))

is_member = input("Are you a member? 'yes' or 'no': ")

if total_bill >= 1000 :
	if is_member == "yes" :
		final_amount = total_bill - (total_bill * 10 / 100)
		print("Final amount is ", final_amount, "with 10% off")
	else :
		final_amount = total_bill - (total_bill * 5 / 100)
		print("Final amount is ", final_amount, "with 5% off")
else :
	print("Final amount is ", total_bill, "with no discount")
