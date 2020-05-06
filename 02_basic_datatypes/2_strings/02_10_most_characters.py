'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

count = 0
list = []
longest_word = ""

while (count<3):
    word = input("Input a word: ")
    list.append(word)
    count = count + 1
    if len(word) > 0:
        longest_word = word

print(str(len(longest_word)) + ", " + longest_word)



