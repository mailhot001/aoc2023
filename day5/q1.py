
# Extract the data
from collections import OrderedDict

output_dict = OrderedDict()
# output_dict['seeds'] = []
output_dict['seed-to-soil'] = {}
output_dict['soil-to-fertilizer'] = {}
output_dict['fertilizer-to-water'] = {}
output_dict['water-to-light'] = {}
output_dict['light-to-temperature'] = {}
output_dict['temperature-to-humidity'] = {}
output_dict['humidity-to-location'] = {}

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
print()

out_step1 = OrderedDict()
for i, seed in enumerate(seeds):
    seed = int(seed)
    if i == 0:
        last_seed = seed

    last_seed = int(last_seed)


    print('seed:', last_seed)
    

    for key in output_dict:
        closest = 0
        # Step 1, search the closest match that is lower
        for step1 in output_dict[key].keys():
            
            if step1 <= seed:
                if (step1 + int(output_dict[key][step1][2]) - 1) >= last_seed:
                    closest = step1
        print('closest', closest)

        # Step 2, check that the step actually contains the value
        if closest != 0:
            print(output_dict[key][closest])
            source, result, extend = output_dict[key][closest]

            out1 = (last_seed - closest) + result

        else: 
            out1 = last_seed
        out_step1[key] = out1
        last_seed = key
    print()
    print('seed', seed)
    for key in out_step1:
        print(key, out_step1[key])

# for key in output_dict:

#     print(key, output_dict[key])# out_step1[key])





        


