


output = {}
with open('./test_input.txt') as the_file:
	input_lines = the_file.readlines()
	for line in input_lines:
		card_and_winning, numbers = line.split('|')
		card_number_raw, winning_numbers = card_and_winning.strip().split(':')
		# print(card_number_raw.split(' '))
		card_number = card_number_raw.split(' ')[-1]
		card_number = card_number.strip()
		numbers = numbers.strip().split(' ')
		winning_numbers = winning_numbers.split(' ')
		numbers_filtered = []
		for number in numbers:
			if number in [' ', '']:
				continue
			else:
				numbers_filtered.append(number)
		winning_numbers_filtered = []
		for winning_number in winning_numbers:
			if winning_number in [' ', '']:
				continue
			else:
				winning_numbers_filtered.append(winning_number)
		output[card_number] = {'winning': winning_numbers_filtered, 'numbers': numbers_filtered}
		print(card_number, winning_numbers_filtered, numbers_filtered,)


total_cards = 0
card_quantity = [1] * 10 #* (len(output.keys())+1)
for key in output.keys():
	print()
	print(key)

	card_winnings = 0
	for number in output[key]['numbers']:
		if number in output[key]['winning']:
			card_winnings += 1

	total_cards += card_quantity[0]

	print(f"points added: win factor: {card_quantity[0]}  card_win: {card_winnings} ({total_cards})")
	
	# print(card_quantity[0])
	this_win_factor = card_quantity.pop(0)
	card_quantity.append(1)
	print(card_quantity)
	for i in range(card_winnings):

		# print(this_win_factor)
		card_quantity[i] += this_win_factor
	print(card_quantity)
	



print(total_cards)


