def get_file_lines(filename):
    file_lines = open(filename, "r").readlines()

    poem_lines_dictionary = {}

    for x in range(len(file_lines)):
        poem_lines_dictionary[x] = file_lines[x]
    
    poem_lines = poem_lines_dictionary.values()
    return(poem_lines)

print(get_file_lines("poem.txt"))

    
