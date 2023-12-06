
# Extract the data


output_dict = {'seeds': [], 'seed-to-soil': {}, 'soil-to-fertilizer': {},
          'fertilizer-to-water': {}, 'water-to-light': {}, 
          'light-to-temperature': {}, 'temperature-to-humidity': {},
          'humidity-to-location': {}, }
current_title = None
with open("./test_input.txt") as the_file:
    input_lines = the_file.readlines()
    for line_no, line in enumerate(input_lines):

        if line_no == 0:
            seeds = line.split(':')[-1].strip().split(' ')
            print('seeds:\n', seeds)

        if line == '\n':
            current_title = None
            continue

        if '-to-' in line:
            title = line.split(' ')[0]
            current_title = title 
        
        elif current_title != None:
            output, input_, extend = line.split(' ')
            input_ = int(input_)
            output = int(output)
            extend = int(extend)
            output_dict[current_title][input_] = [input_, output, extend]


print(output_dict)


for seed in seeds:
    print('seed:', seed)
    closest = 0
    # Step 1, search the closest match that is lower
    for step1 in output_dict['seed-to-soil'].keys():
        if step1 <= seed and step1 < closest:
            closest = step1

    # Step 2, check that the step actually contains the value
    
    source, result, extend = output_dict['seed-to-soil'][step1]
    





        

