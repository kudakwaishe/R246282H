import random


random_numbers = [random.randint(1, 100) for _ in range(10)]

# Run bit
print(f"Generated numbers: {random_numbers}")


if random_numbers:
    average = sum(random_numbers) / len(random_numbers)
    print(f"The average of the numbers is: {average}")
else:
    print("The list is empty.")
