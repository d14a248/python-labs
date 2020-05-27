'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
numbers = []
while True:
    item = input("Enter a number (type 'done' when finished): ")
    if item == "done":
        break
    elif item.isdigit():
        numbers.append(int(item))
if len(numbers) % 2 != 0:
    numbers.append(0)
print("A list of your numbers: " + str(numbers))
tuple_numbers = [(num1,) for num1  in sorted(numbers)]
# not sure why [tuple(number) for number in sorted(numbers)] does not work
# did something similar in 03_16_list_of_tuples
print("Your numbers sorted as tuples: " + str(tuple_numbers))
final_numbers = [tuple_numbers[i] + tuple_numbers[i+1] for i in range(0,len(tuple_numbers),2)]
print("Your numbers paired as tuples: " + str(final_numbers))



    


