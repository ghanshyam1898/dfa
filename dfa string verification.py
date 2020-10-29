# Format of route map : [(initial_state, alphabet, final_state), (...), (...)]

route_map = []

# Build route map starts

allowed_alphabets = input("Enter the allowed alphabets (separated by spaces) : ").split()
raw_all_states = input("Enter all the names of states (separated by spaces) : ")
all_states = raw_all_states.split()

raw_final_states = input("Enter all the names FINAL states (separated by spaces) : ")
final_states = raw_final_states.split()

for alphabet in allowed_alphabets:
	for state in all_states:
		next_state = input("Enter the next state for {} with {} : ".format(state, alphabet))
		if len(next_state) > 0:
			route_map.append((state, alphabet, next_state))
		else:
			print("\nState rejected\n")

while True:
	string = input("\nEnter the string : ")

	currently_alphabet_index = 0
	current_state = 'q0'
	allowed_routes_for_current_state = []

	for alphabet in string:
		
		# find out the alphabets allowed at the current state
		for item in route_map:
			if item[0] == current_state:
				allowed_routes_for_current_state.append(item)

		was_able_to_reach_next_state = False
		for item in allowed_routes_for_current_state:
			if item[1] == alphabet:
				current_state = item[2]
				was_able_to_reach_next_state = True

		if was_able_to_reach_next_state is False:
			input("Invalid string.\nPress enter  : ")
			continue

		allowed_routes_for_current_state = []

	if current_state in final_states:
		input("String Valid.\nPress enter : ")

	else:
		input("Invalid string.\nPress enter : ")
