'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

numbers = []
sum = 0

for i in range(10):
    number = int(input("Input a whole number: "))
    numbers.append(number)
    sum += number

print("Your numbers are the following: " + str(numbers))
print("The largest number is: " + str(max(numbers)))
print("The sum of your numbers is: " + str(sum))
