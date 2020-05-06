'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
first_name_translated = first_name[1:].capitalize() + first_name[0].lower() + "ay"
last_name_translated = last_name[1:].capitalize() + last_name[0].lower() + "ay"
print("You are now renamed as: " + first_name_translated + " " + last_name_translated)
