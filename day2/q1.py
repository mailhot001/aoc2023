

with open('./input.txt') as the_file:
	all_lines = the_file.readlines()
	cubes_limits = {'red': 12, 'green': 13, 'blue': 14}
	possible_game_ids = []


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
			for key in cube_max.keys():
				if cube_max[key] <= cubes_limits[key]:
					continue
				else:
					possible = False
					break

		if possible == True:
			possible_game_ids.append(int(game_num))
		print(game_num, possible, )
		print(cube_max)
		print()

total_sum = 0
for possible_game_id in possible_game_ids:
	total_sum += possible_game_id

print(total_sum)