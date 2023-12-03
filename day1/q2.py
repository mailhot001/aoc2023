


num_dict = {'one': 1, 
            'two': 2, 
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8, 
            'nine': 9,
            }

with open('./input.txt') as the_file:
    lines = the_file.readlines()

    value_list = []
    for i, line in enumerate(lines):
        index_min = len(line)-1 
        index_max = 0
        print()
        print(line)
        print(i)
        for index_, element in enumerate(line):
            try:
                int_element = int(element)
                value1 = int_element
                index_value1 = index_
                print(index_, value1)
                break
            except:
                continue

        for key in num_dict.keys():
            string_num1 = line.find(key, )
            if string_num1 == -1:
                continue

            elif string_num1 < index_min:
                index_min = string_num1
                number_min = num_dict[key]
                
            else: 
                continue
        print(index_min, number_min)

        if index_min < index_value1:
            value1_out = number_min
        elif index_min >= index_value1:
            value1_out = value1

        print('value1_out', value1_out)

        print('------')
        for index_, element in enumerate(reversed(line)):
            try:
                int_element = int(element)
                value2 = int_element
                print((len(line)-index_-1), value2)
                index_value2 = len(line)-index_-1
                break
            except:
                continue
        for key in num_dict.keys():
            string_num2 = line.rfind(key,)
            if string_num2 == -1:
                continue
            elif string_num2 > index_max:
                index_max = string_num2  #trouve la fin du mot
                number_max = num_dict[key]
            else: 
                continue
        print(index_max, number_max)

        if index_max > index_value2:
            value2_out = number_max
        elif index_max <= index_value2:
            value2_out = value2

        current_value = value1_out * 10 + value2_out
        print(current_value)
        value_list.append(current_value)

total = 0
for element in value_list:
    total += element

print(total)