#6:35 -




with open('./input.txt') as the_file:
    lines = the_file.readlines()

    value_list = []
    for i, line in enumerate(lines):
        print()
        print(line)
        print(i)
        for index_, element in enumerate(line):
            try:
                int_element = int(element)
                value1 = int_element
                print(index_, value1)
            except:
                continue
        print('------')
        for index_, element in enumerate(reversed(line)):
            try:
                int_element = int(element)
                value2 = int_element
                print((len(line)-index_-1), value2)
            except:
                continue
        current_value = value2 * 10 + value1
        print(current_value)
        value_list.append(current_value)

total = 0
for element in value_list:
    total += element

print(total)