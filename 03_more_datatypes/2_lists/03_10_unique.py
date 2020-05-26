'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]

'''

unique_list = []
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

print("This is the original list: " + str(list_))

for item in range(len(list_)):
    if list_.count(list_[item]) == 1:
        unique_list.append(list_[item])

# [unique_list.append(item) for item in list_ if list_.count(list_[item]) == 1]
# not sure why this list comprehension does not work

print("This is the unique list:   " + str(unique_list))
