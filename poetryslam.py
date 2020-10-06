import random
line_list = []
def get_file_lines(filename):
    file_lines = open(filename, "r").readlines()

    poem_lines_dictionary = {}

    for x in range(len(file_lines)):
        poem_lines_dictionary[x] = file_lines[x]

    
    for x in range(len(poem_lines_dictionary)):
        print(poem_lines_dictionary[x])
        line_list.append(poem_lines_dictionary[x])
    
    return line_list


get_file_lines("poem.txt")

def lines_printed_backwards(lines_list):
    for x in reversed(range(len(lines_list))):
        print(str(x + 1) + " " + line_list[x])

lines_printed_backwards(line_list)

def lines_printed_random(lines_list):
    counter = []
    for x in range(len(lines_list)):
        counter.append(x)
    for x in range(len(lines_list)):
        randomNumber = random.randint(0, len(counter) - 1)
        print(str(counter[randomNumber] + 1) + " " + lines_list[counter[randomNumber]])
        counter.pop(randomNumber)

lines_printed_random(line_list)
        







