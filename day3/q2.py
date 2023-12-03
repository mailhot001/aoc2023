
# data format for analysis
# (index, number)

import re
symbol_set = set()
confirmed_number = []
processed_index = []
output = {}
with open('./input.txt') as the_file:
	lines = the_file.readlines()
	data_num = [] # 3 lines list to analyse
	data_symbol = []

	for line_no, line in enumerate(lines):
		#line = line.replace('.', ' ')
		print()
		numbers = {m.start(0):int(m.group(0)) for m in re.finditer("\d+", line)}
		print(line_no, numbers)

		symbols = {m.start(0):m.group(0) for m in re.finditer("[$&+/,:;=?@#|'<>^*()%!-]", line)}
		for key in symbols.keys():
			symbol_set.add(symbols[key])

		print('   ', symbols)

		# data_num.append(numbers)
		# data_symbol.append(symbols)
		output[line_no] = {'number': numbers, 'symbols': symbols}
		
print("----------------data----------------")

# check the line for proximity
for index, output_key in enumerate(output.keys()):
	print(index)
	confirmed_number_filter = [False] * len(output[output_key]['number'])
	# print(confirmed_number_filter)
	

	for number_index, symbol_key in enumerate(output[output_key]['symbols'].keys()):

		# Search for the proper symbol
		if output[output_key]['symbols'][symbol_key] == '*':
			temp_confirmed_number = []
			star_key = symbol_key


			for number_key in output[output_key]['number'].keys():
				# define the range of number
				min_ = number_key - 1
				max_ = number_key + len(str(output[output_key]['number'][number_key]))
				if star_key >= min_ and star_key <= max_:
					temp_confirmed_number.append(output[output_key]['number'][number_key])
		
			# check preceding line if any
			if index > 0:
				for number_key in output[output_key-1]['number'].keys():
					# define the range of number
					min_ = number_key - 1
					max_ = number_key + len(str(output[output_key-1]['number'][number_key]))
					if star_key >= min_ and star_key <= max_:
						temp_confirmed_number.append(output[output_key-1]['number'][number_key])
		

			# Check following line if any
			if index < (len(output.keys())-1):
				for number_key in output[output_key+1]['number'].keys():
					# define the range of number
					min_ = number_key - 1
					max_ = number_key + len(str(output[output_key+1]['number'][number_key]))
					if star_key >= min_ and star_key <= max_:
						temp_confirmed_number.append(output[output_key+1]['number'][number_key])
		


			if len(temp_confirmed_number) == 2:
				gear_ratio = temp_confirmed_number[0] * temp_confirmed_number[1]
				print(temp_confirmed_number)
				confirmed_number.append(gear_ratio)





total = 0
for number in confirmed_number:
	total += number
print(total)


 
