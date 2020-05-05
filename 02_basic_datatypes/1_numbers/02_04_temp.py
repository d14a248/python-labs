'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

import math

f = float(input("Enter the temperature in Fahrenheit: "))
c = (f - 32) * (5 / 9)

print(str(f) + " degrees fahrenheit = " + str((f - 32) * (5 / 9)))
#works as expected for 81.32 but needs to round for other inputed teperatures