import math

def add_str(in_string,value,offset):
    in_str_len = len(in_string)
    value_len = len(str(value))
    left_edge = in_str_len - offset - value_len - 1
    right_edge = in_str_len - offset
    string_segment = in_string[left_edge: right_edge]
    new_segment = str(int(string_segment) + value)
    return in_string[:left_edge + 1] + new_segment + in_string[right_edge:]

#load data from file
data = []
with open('013_data.txt', 'r') as input:
    eof = False
    while not eof:
        datum = input.readline()
        if datum == "": eof = True
        else: data.append(datum[:-1])

#sum each column then add each individual total
lines = len(data)
cols = len(data[0])
total_str = "0"*(cols + int(math.log10(lines))+1)
i=0
for col in range(cols-1,-1,-1):
    local_sum = 0
    for line in range(lines):
        local_sum += int(data[line][col])
    total_str = add_str(total_str, local_sum, i)
    i += 1

print total_str
