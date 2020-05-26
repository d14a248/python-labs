'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flat_list = []
for list in starting_list:
    for item in list:
        flat_list.append(item)
print("This is the starting list: " + str(starting_list))
print("And this is the flattened list: " + str(flat_list))

#flat = [item for list in starting_list for item in list]
#print(flat)
