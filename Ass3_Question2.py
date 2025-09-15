def calculate_average(*args):

    # Check if no numbers were provided
    if not args:
        return 0

    # Calculate and return the average
    return sum(args) / len(args)



# Example

print(calculate_average(2, 4, 6))
print(calculate_average(10, 20))
print(calculate_average(5))
print(calculate_average())
