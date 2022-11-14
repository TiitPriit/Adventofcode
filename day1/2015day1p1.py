import re

input_string = 'input.txt'

with open(input_string, 'r') as input_file:
    for line in input_file:

        open_parens = re.findall(r'\(', line)
        close_parens = re.findall(r'\)',line)

        open_parens_count = len(open_parens)
        close_parens_count = len(close_parens)

        floor = open_parens_count - close_parens_count
        print("Santa, go to floor " + str(floor))

input_file.close()