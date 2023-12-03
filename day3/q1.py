
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
	temp_confirmed_number = []

	for number_index, number_key in enumerate(output[output_key]['number'].keys()):

		# check along this line for proximity
		min_ = number_key - 1
		max_ = number_key + len(str(output[output_key]['number'][number_key]))

		if len(output[output_key]['symbols']) > 1:
			for symbol_key in output[output_key]['symbols'].keys():
				if symbol_key >= min_ and symbol_key <= max_:
					# confirmed_number.append(output[output_key]['number'][number_key])
					confirmed_number_filter[number_index] = True
					#print(index, output[output_key]['number'][number_key], output[output_key]['symbols'][symbol_key])
			# if confirmed_number_filter[number_index] == True:
			# 	continue
		
		# check preceding line if any
		if index > 0:
			if len(output[output_key-1]['symbols']) > 1:
				for symbol_key in output[output_key-1]['symbols'].keys():
					if symbol_key >= min_ and symbol_key <= max_:
						# confirmed_number.append(output[output_key]['number'][number_key])
						confirmed_number_filter[number_index] = True
						#print(index, output[output_key]['number'][number_key], output[output_key]['symbols'][symbol_key])
				# if confirmed_number_filter[number_index] == True:
				# 	continue

		# Check following line if any
		if index < (len(output.keys())-1):
			if len(output[output_key+1]['symbols']) > 1:
				for symbol_key in output[output_key+1]['symbols'].keys():
					if symbol_key >= min_ and symbol_key <= max_:
						# confirmed_number.append(output[output_key]['number'][number_key])
						confirmed_number_filter[number_index] = True
						#print(index, confirmed_number[-1], output[output_key]['symbols'][symbol_key])
				# if confirmed_number_filter[number_index] == True:
				# 	continue
		if confirmed_number_filter[number_index] == True:
			temp_confirmed_number.append(output[output_key]['number'][number_key])
		elif confirmed_number_filter[number_index] == False:
			temp_confirmed_number.append(0)
	print(confirmed_number_filter)
	print(temp_confirmed_number)
	confirmed_number += temp_confirmed_number
	print()


total = 0
for number in confirmed_number:
	total += number
print(total)


 
