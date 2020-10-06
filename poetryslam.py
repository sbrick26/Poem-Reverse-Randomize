def get_file_lines(filename):
    file_lines = open(filename, "r").readlines()

    poem_lines_dictionary = {}

    for x in range(len(file_lines)):
        poem_lines_dictionary[x] = file_lines[x]

    line_list = []
    for x in range(len(poem_lines_dictionary)):
        print(poem_lines_dictionary[x])


get_file_lines("poem.txt")



