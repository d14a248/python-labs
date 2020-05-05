'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
f = 3.0 #float
i = 5 #int
i2f = float(i) #convert int to float
f2i = int(f) # convert float to int

print ("The integer " + str(i) + " is converted to a float: " + str(i2f))
print ("The float " + str(f) + " is converted to an integer: " + str(f2i)) #loses the info after decimal point

print ("Floor division: 5//3.0 equals: " + str(i//5)) #loses the info after the decimal point

#only works with two integers not an integer and float
n1 = int(input("Choose an integer for multiplication: "))
n2 = int(input("Choose another integer multiplication: "))
a = n1*n2
print(str(n1) + " multiplied by " + str(n2) + " equals: " + str(a))




