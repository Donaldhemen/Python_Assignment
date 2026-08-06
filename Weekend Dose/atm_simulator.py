balance = 100000

while(True):
	atm_menu = """
== Welcome to ATM Menu ==
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
"""
	print(atm_menu)
	atm_menu_choice = int(input())

	match(atm_menu_choice):
		case 1: 
			deposit = int(input("Enter deposit amount: "))
			balance = deposit + balance
			print("Balance is: ", balance)
		case 2:
			withdraw = int(input("Enter withdraw amount: "))
			if balance >= withdraw:
				balance = balance - withdraw
				print("Balance is: ", balance)
			else :
				print("Insufficient funds")
		case 3:
			print("Balance is: ",balance)
		case 4:
			print("Goodbye")
			break

