from time import time

def zeros(n):
    count = 0
    starttime = time()  # Start the timer
    
    for multiplier in range(1, n+1):
        num = multiplier
        
        while num > 0:
            if num % 10 == 0:
                count += 1
            num //= 10
    
    end_time = time()  # End the timer
    execution_time = end_time - starttime

    
    return count

# Taking input from the user
target = int(input("Enter the target number: "))

starttime = time()
zeros_count = zeros(target)
end_time = time()

execution_time = end_time - starttime

print(f"The number of zeros from 1 to {target} is: {zeros_count}")
print(f"Total execution time: {execution_time} seconds")


