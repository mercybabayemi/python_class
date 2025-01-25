nokia_menu = int(input("""Nokia menu
1. Phonebook
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
"""))

match nokia_menu:
	case 1: 
		phonebook = int(input("""Phonebook
		1. Search
		2. Service Nos
		3. Add name
		4. Erase 
		5. Edit
		6. Assign tones
		7. Send b'card
		8. Options
		9. Speed dials
		10. Voice tags
		"""))
			
		match phonebook:
			case 1: print("Search")
			case 2: print("Service NoS.")
			case 3: print("Add name")
			case 4: print("Erase")
			case 5: print("Edit")
			case 6: print("Assign tone")
			case 7: print("Send b'card")
			case 8: 
				options = int(input("""Options
				1. Type of view
				2. Memory status
				"""))

				match options:
					case 1: print("Type of view")
					case 2: print("Memory status")
			case 9: print("Speed dials")
			case 10: print("Voice tags")


	case 2: 
		messages = int(input("""Messages
		1. Write message
		2. Inbox
		3. Outbox
		4. Picture messages
		5. Templates
		6. Smileys
		7. Message settings
		8. Info service
		9. Voice mailbox number
		10. Service command editor
		"""))

		match messages:
			case 1: print("Write messages")
			case 2: print("Inbox")
			case 3: print("Outbox")
			case 4: print("Picture messages")
			case 5: print("Templates")
			case 6: print("Smileys")
			case 7: 
				message_settings = int(input("""
				Message Settings
				1. Set 1
				2. Common
				"""))

				match message_settings:
					case 1: 
						set_one = int(input("""Set 1
						1.Message centre number 
						2. Message sent as
						3. Message validity
						"""))

						match set_one:
							case 1: print("Message centre number")
							case 2: print("Message sent as")
							case 3: print("Message validity")
					case 2:
						common = int(input("""Common
						1.Delivery report
						2. Reply via same centre
						3. Character support
						"""))
						match common:
							case 1: print("Delivery report")
							case 2: print("Reply via same centre")				
							case 3: print("Character support")				
			case 8: print("Info service")
			case 9: print("Voice mailbox number")
			case 10: print("Service command editor")

	case 3: print("Chat")
	case 4: 
		call_register = int(input("""Call register
		1. Missed call
		2. Received calls
		3. Dialled numbers
		4. Erase recent call lists
		5. Show call duration 
		6. Show call cost
		7. Call cost settings
		8. Prepaid credit
		"""))
		match call_register:
			case 1: print("Missed calls")
			case 2: print("Received calls")
			case 3: print("Dialled numbers")
			case 4: print("Erase recent call lists")
			case 5:
				show_call_duration = int(input("""Show call duration
				1. Last call duration
				2. All calls' duration
				3. Received calls' duration
				4. Dialed calls' duration
				5. Clear timers
				"""))
				match show_call_duration:
					case 1: print("Last call duration")
					case 2: print("All calls' duration")
					case 3: print("Received calls' duration")
					case 4: print("Dialed calls' duration")
					case 5: print("Clear timers")
			case 6: 
				show_call_costs = int(input("""Show call costs
				1. Last call cost
				2. All calls' cost
				3. Clear counters
				"""))
				match showCallCosts:
					case 1: print("Last call cost")
					case 2: print("All calls' cost")
					case 3: print("Clear counters")
			case 7: 
				call_cost_settings = int(input("""Call cost settings
				1. Call cost limits
				2. Show costs in
				"""))
				match call_cost_settings:
					case 1: print("Call cost limits")
					case 2: print("Show costs in")
			case 8: print("Prepaid credit")


	case 5: 
		tones = int(input("""Tones
		1. Ringing tone
		2. Ringing volume
		3. Incoming call alert
		4. Composer
		5. Message alert tone
		6. Keypad tones
		7. Warning and games tones
		8. Vibrating alert
		9. Screen saver	
		"""))
		match tones:
			case 1: print("Ringing tone")
			case 2: print("Ringing volume")
			case 3: print("Incoming call alert")
			case 4: print("Composer")
			case 5: print("Message alert tone")
			case 6: print("Keypad tones")
			case 7: print("Warning and games tones")
			case 8: print("Vibrating alert");		
			case 9: print("Screen saver")
	case 6:
		settings = int(input("""Settings
		1. Call settings
		2. Phone settings
		3. Security settings
		4. Restore factory settings
		"""))
		match settings:
			case 1:
				call_settings = int(input("""Call settings
				1. Automatic redial
				2. Speed dialing
				3. Call waiting options
				4. Own number sending
				5. Phone line in use
				6. Automatic answer
				"""))
	
				match call_settings:
					case 1: print("Automatic redial")
					case 2: print("Speed dialing")
					case 3: print("Call waiting options")
					case 4: print("Own number sending")
					case 5: print("Phone line in use")
					case 6: print("Automatic answer")
			case 2: 
				call_settings = int(input("""Phone settings
				1. Language
				2. Cell info display
				3. Welcome note
				4. Network selection
				5. Lights
				6. Confirm SIM service actions
				"""))
				match phone_settings:
					case 1: print("Language")
					case 2: print("Cell info display")
					case 3: print("Welcome note")
					case 4: print("Network selection")
					case 5: print("Lights")
					case 6: print("Confirm SIM service actions")
			case 3:
				security_settings = int(input("""Security settings
				1. PIN code request
				2. Call barring service
				3. Fixed dialing
				4. Closed user group
				5. Phone security
				6. Change access codes
				"""))
				match security_settings:
					case 1: print("PIN code request")
					case 2: print("Call barring service")
					case 3: print("Fixed dialing")
					case 4: System.out.print("Closed user group")
					case 5: print("Phone security")
					case 6: print("Change access codes")
					case 4: print("Restore factory settings")
	case 8: System.out.print("Games")
	case 9: System.out.print("Calculator")
	case 10: System.out.print("Reminders")
	case 11: 
		security_settings = int(input("""Clock
		1. Alarm clock
		2. Clock settings
		3. Date setting
		4. Stopwatch
		5. Countdown timer
		6. Auto update of date and time
		"""))
		match clock:
			case 1: System.out.print("Alarm clock")
			case 2: System.out.print("Clock settings")
			case 3: System.out.print("Date setting")
			case 4: print("Stopwatch")
			case 5: print("Countdown timer")
			case 6: System.out.print("Auto update of date and time")
	case 12: print("Profiles")
	case 13: print("SIM services")