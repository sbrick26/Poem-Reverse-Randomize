import random
line_list = []
def get_file_lines(filename):
    #open file to read
    file_lines = open(filename, "r").readlines()

    poem_lines_dictionary = {}

    #adds files to dict
    for x in range(len(file_lines)):
        poem_lines_dictionary[x] = file_lines[x]

    #gets lines
    for x in range(len(poem_lines_dictionary)):
        #print(poem_lines_dictionary[x])
        line_list.append(poem_lines_dictionary[x])
    
    return line_list


get_file_lines("poem.txt")


def lines_printed_backwards(lines_list):
    #for loop that goes through indexs backwards
    for x in reversed(range(len(lines_list))):
        print(str(x + 1) + " " + line_list[x])

print("\nBACKWARDS POEM:\n")
lines_printed_backwards(line_list)

def lines_printed_random(lines_list):
    counter = []
    #set list to count used indexs to not repeat lines
    for x in range(len(lines_list)):
        counter.append(x)
    #prints random line and removes index from list
    for x in range(len(lines_list)):
        randomNumber = random.randint(0, len(counter) - 1)
        print(str(counter[randomNumber] + 1) + " " + lines_list[counter[randomNumber]])
        counter.pop(randomNumber)

print("\nRANDOM POEM:\n")
lines_printed_random(line_list)

def lines_printed_custom(lines_list):
    #odds first evens second

    #odds with mod
    for x in range(len(lines_list)):
        if x%2==0:
            print(str(x+1) + " " + lines_list[x])
    #evens with mod
    for x in range(len(lines_list)):
        if x%2!=0:
            print(str(x+1) + " " + lines_list[x])

print("\nODDS AND EVENS POEM: \n")
lines_printed_custom(line_list)

        







