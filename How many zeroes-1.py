#########################################################
#Name - Satyendra Raj Singh
#date-12/6/2013
#description- Program to find how many zeroes
##########################################################

from time import time
# function to count number of zeroes 
# from 1 to desired number
def zeros(n):
    count = 0 #counter  setup
    starttime = time()  # Start the timer
    for number in range(1, n+1):
        n = number
        while n > 0:
            counter = n % 10
            if counter == 0:
                count += 1
            n //= 10
    stoptime = time()  # End the timer
    elapsed_time = stoptime - starttime
    return count

# Taking input from the user
AimNumber = int(input("What number do you want to count zeros to? "))

starttime = time()
countzero = zeros(AimNumber)
stoptime = time()

elapsed_time = stoptime - starttime
print(f"The number of zeros from 1 to {AimNumber} is: {countzero}")
print(f"Total execution time: {elapsed_time} seconds")
