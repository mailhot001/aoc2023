

with open('./input.txt') as the_file:
	all_lines = the_file.readlines()
	cubes_limits = {'red': 12, 'green': 13, 'blue': 14}
	game_powers = []


	for line in all_lines:
		possible = True
		cube_max = {'red': 0, 'green': 0, 'blue': 0}
		game, tests_str = line.split(':')
		game_num = game.strip('Game ')
		tests = tests_str.split(';')

		for test in tests:
			draws = test.split(',')
			for draw in draws:
				quantity, color = draw.strip().split(' ')
				quantity = int(quantity)
				if cube_max[color] < quantity:
					cube_max[color] = quantity
			
		power = cube_max['red'] * cube_max['green'] * cube_max['blue']
		game_powers.append(power)
		print(game_num, )
		print(power, cube_max)
		print()

total_sum = 0
for game_power in game_powers:
	total_sum += game_power

print(total_sum)