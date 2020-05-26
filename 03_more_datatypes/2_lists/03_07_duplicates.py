'''

Write a script that removes all duplicates from a list.

'''


list_ = [1, 2, 3, 4, 3, 4, 5]
new_list = []
[new_list.append(item) for item in list_ if item not in new_list]
print(new_list)

