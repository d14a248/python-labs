'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

principle = int(input("How much is your initial investment amount: "))
interest = int(input("What is the interest rate: "))
years = int(input("How many years will you be investing: "))
print("At an initial investment of $" + str(principle) + " at a rate of " + str(interest) + "% for " + str(years) + " years, compounded annually, your return will be $" + str(principle*((1+interest/100)**years)))


