


output = {}
with open('./input.txt') as the_file:
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
points = 0
for key in output.keys():
	card_points = 0
	for number in output[key]['numbers']:
		if number in output[key]['winning']:
			if card_points == 0:
				card_points +=1
			else:
				card_points = card_points * 2
	points += card_points

print(points)


