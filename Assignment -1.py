import time


class ZeroCounter:

    def __init__(self, target):

        self.name = target


    def count_zeros(self):

        start_time = time.time()

        count = 0

        for i in range(1, self.name + 1):
            num = i

            while num > 0:

                if num % 10 == 0:

                    count += 1

                num //= 10

        end_time = time.time()

        time_taken = end_time - start_time

        return count, time_taken


# Taking input from the user

target_value = int(input("Enter the target value: "))


zero_counter = ZeroCounter(target_value)

zeros_count, time_taken = zero_counter.count_zeros()


print(f"Number of zeros from 1 to {target_value}: {zeros_count}")

print(f"Time taken: {time_taken} seconds")

