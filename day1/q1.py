


with open('./input.txt') as the_file:
    lines = the_file.readlines()

    value_list = []
    for i, line in enumerate(lines):
        print(line)
        print()
        print(i)
        for element in line:
            try:
                int_element = int(element)
                value1 = int_element
                print(value1)
            except:
                continue
        for element in reversed(line):
            try:
                int_element = int(element)
                value2 = int_element
                print(value2)
            except:
                continue
        current_value = value2 * 10 + value1
        print(current_value)
        value_list.append(current_value)

total = 0
for element in value_list:
    total += element

print(total)