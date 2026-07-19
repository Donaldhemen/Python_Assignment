# 

main_menu = """
List of menu functions

1. Phone book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
"""
print(main_menu)
main_menu_choice = int(input())

match main_menu_choice :
	case 1 : 
		print("Phone book")
		phone_book_menu = """

1. Search
2. Service Nos 
3. Add name 
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
"""
		print(phone_book_menu)
		phone_book_menu_choice = int(input())

		match phone_book_menu_choice :
			case 1 : 
				print("Search")
			case 2 : 
				print("Service Nos")
			case 3 : 
				print("Add name")
			case 4 : 
				print("Erase")
			case 5 : 
				print("Edit")
			case 6 : 
				print("Assign tone")
			case 7 : 
				print("Send b'card")
			case 8 : 
				print("Options")
				options_menu = """

1. Type of view
2. Memory status
"""
				print(options_menu)
				options_menu_choice = int(input())

				match(options_menu_choice) :
					case 1 : 
						print("Type of view")
					case 2 : 
						print("Memory status")
					case _:
						print("Invalid input")
				
			case 9 : 
				print("Speed dials")
			case 10 : 
				print("Voice tags")
			case _:
				print("Invalid input")

	case 2 : 
		print("Messages")
		messages_menu = """

1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Service
9. Voice mailbox number
10. Service command editor
"""
		print(messages_menu)
		messages_menu_choice = int(input())

		match(messages_menu_choice):
			case 1 : 
				print("Write messages")
			case 2 : 
				print("Inbox")
			case 3 : 
				print("Outbox")
			case 4 : 
				print("Picture messages")
			case 5 : 
				print("Templates")
			case 6 : 
				print("Smileys")
			case 7 : 
				print("Message settings") 
				messages_settings_menu = """
1. Set 1
2. Common
"""
				print(messages_settings_menu)
				messages_settings_menu_choice = int(input())

				match(messages_settings_menu_choice) : 
					case 1 : 
						print("Set 1")
						set1_menu = """
1. Message centre Number
2. Messages sent as
3. Message validity
"""
						print(set1_menu)
						set1_menu_choice = int(input())

						match(set1_menu_choice) :
							case 1 : 
								print("Message centre Number")
							case 2 : 
								print("Messages sent as")
							case 3 : 
								print("Message validity")
							case _:
								print("Invalid input")
					case 2 :
						print("Common") 
						common_menu = """
1. Delivery reports
2. Reply via same centre
3. Character support
"""
						print(common_menu)
						common_menu_choice = int(input())

						match(common_menu_choice) : 
							case 1 : 
								print("Delivery reports")
							case 2 : 
								print("Reply via same centre")
							case 3 : 
								print("Character support")
							case _:
								print("Invalid input")
		
					case _:
						print("Invalid input")

			case 8 : 
				print("Info Service")
			case 9 : 
				print("Voice mailbox number")
			case 10 : 
				print("Service command editor")
			case _:
				print("Invalid input")

	case 3 :
		print("Chat")
	case 4 : 
		print("Call Register")
		call_register_menu = """

1. Missed calls
2. Recieved calls
3. Dialled calls
4. Erase recent calls lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
"""
		print(call_register_menu)
		call_register_menu_choice = int(input())

		match(call_register_menu_choice) :
			case 1 : 
				print("Missed calls")
			case 2 : 
				print("Recieved calls")
			case 3 : 
				print("Dialled calls")
			case 4 : 
				print("Erase recent calls lists")
			case 5 : 
				print("Show call duration") 
				show_call_duration_menu = """
1. Last call duration
2. All calls duration
3. Recieved calls duration
4. Dialled calls duration
5. Clear timers
"""
				print(show_call_duration_menu)
				show_call_duration_menu_choice = int(input())

				match(show_call_duration_menu_choice) :
					case 1 : 
						print("Last call duration")
					case 2 : 
						print("All calls duration")
					case 3 : 
						print("Recieved calls duration")
					case 4 : 
						print("Dialled calls duration")
					case 5 : 
						print("Clear timers")
					case _:
						print("Invalid input")

			case 6 : 
				print("Show call costs") 
				show_call_costs_menu = """
1. Show last call costs
2. All calls costs
3. Clear counters
"""
				print(show_call_costs_menu)
				show_call_costs_menu_choice = int(input())

				match(show_call_costs_menu_choice) :
					case 1 : 
						print("Show last call costs")
					case 2 : 
						print("All calls costs")
					case 3 : 
						print("Clear counters")
					case _:
						print("Invalid input")
			
			case 7 : 
				print("Call cost settings") 
				call_cost_settings_menu = """
1. Call cost limit
2. Show costs in
"""
				print(call_cost_settings_menu)
				call_cost_settings_menu_choice = int(input())

				match(call_cost_settings_menu_choice) :
					case 1 : 
						print("Call cost limit")
					case 2 : 
						print("Show costs in")
					case _:
						print("Invalid input")
					
			case 8 : 
				print("Prepaid credit")
			case _:
				print("Invalid input")

	case 5 :
		print("Tones")
		tones_menu ="""
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
"""
		print(tones_menu)
		tones_menu_choice = int(input())

		match(tones_menu_choice) :
			case 1 : 
				print("Ringing tone")
			case 2 : 
				print("Ringing volume")
			case 3 : 
				print("Incoming call alert")
			case 4 : 
				print("Composer")
			case 5 : 
				print("Message alert tone")
			case 6 : 
				print("Keypad tones")
			case 7 : 
				print("Warning and game tones")
			case 8 : 
				print("Vibrating alert")
			case 9 : 
				print("Screen saver")
			case _:
				print("Invalid input")
			
	case 6 :
		print("Settings")
		settings_menu = """
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
"""
		print(settings_menu)
		settings_menu_choice = int(input())

		match(settings_menu_choice) :
			case 1 : 
				print("Call settings")
				call_settings_menu = """
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
"""
				print(call_settings_menu)
				call_settings_menu_choice = int(input())

				match(call_settings_menu_choice) :
					case 1 : 
						print("Automatic redial")
					case 2 : 
						print("Speed dialling")
					case 3 : 
						print("Call waiting options")
					case 4 : 
						print("Own number sending")
					case 5 : 
						print("Phone line in use")
					case 6 : 
						print("Automatic answer")
					case _: 
						print("Invalid input")
					
			case 2 : 
				print("Phone settings")
				phone_settings_menu = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
"""
				print(phone_settings_menu)
				phone_settings_menu_choice = int(input())

				match(phone_settings_menu_choice) :
					case 1 : 
						print("Language")
					case 2 : 
						print("Cell info display")
					case 3 : 
						print("Welcome note")
					case 4 : 
						print("Network selection")
					case 5 : 
						print("Lights")
					case 6 : 
						print("Confirm SIM service actions")
					case _:
						print("Invalid input")
				
			case 3 : 
				print("Security settings")
				security_settings_menu = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
"""
				print(security_settings_menu)
				security_settings_menu_choice = int(input())

				match(security_settings_menu_choice) :
					case 1 : 
						print("PIN code request")
					case 2 : 
						print("Call barring service")
					case 3 : 
						print("Fixed dialling")
					case 4 : 
						print("Closed user group")
					case 5 : 
						print("Phone security")
					case 6 : 
						print("Change access codes")
					case _: 
						print("Invalid input")
				
			case 4 : 
				print("Restore factory settings")
			case _:
				print("Invalid input")
			
	case 7 : 
		print("Call divert")
	case 8 :
		print("Games")
	case 9 :
		print("Calculator")
	case 10 :
		print("Reminders")
	case 11 :
		print("Clock")
		clock_menu = """
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
"""
		print(clock_menu)
		clock_menu_choice = int(input())

		match(clock_menu_choice) :
			case 1 : 
				print("Alarm clock")
			case 2 : 
				print("Clock settings")
			case 3 : 
				print("Date settings")
			case 4 : 
				print("Stopwatch")
			case 5 : 
				print("Countdown timer")
			case 6 : 
				print("Auto update of date and time")
			case _: 
				print("Invalid input")

	case 12 : 
		print("Profiles")
	case 13 :
		print("SIM services")
	case _:
		print("Invalid input")