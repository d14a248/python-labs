'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string = input("Input a string: ")
print("A string: " + string)
result_list = [tuple(word) for word in string.split()]
print("A list of tuples: " + str(result_list))