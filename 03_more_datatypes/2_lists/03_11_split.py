'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
string = input("Input a string: ") #get the string from the user

string_split = string.lower().split() #split the string by the words into a list and make all characters lower case

string_count = [string_split.count(item) for item in string_split] #count the occurances of each word

string_dictionary = dict(zip(string_split, string_count)) #combine the list of words and the list of occurances into a dictionary

max_value = max(string_dictionary.values()) #find the max value in the dictionary

max_keys = [key for key, value in string_dictionary.items() if value == max_value] #find the associated key to the max value
print("The following word(s) have the most occurances: " + str(max_keys))


