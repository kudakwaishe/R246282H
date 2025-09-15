def divide_numbers(numerator, denominator):
    """
    Divides two numbers, handling ZeroDivisionError and TypeError.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")
        return None

# Run bit
print(f"Result of 10 / 2: {divide_numbers(10, 2)}")
print(f"Result of 10 / 0: {divide_numbers(10, 0)}")
print(f"Result of 'a' / 2: {divide_numbers('a', 2)}")
