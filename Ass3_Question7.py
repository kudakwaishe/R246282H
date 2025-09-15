class NegativeNumberError(Exception):

    pass

def check_positive(number):

    if number < 0:
        raise NegativeNumberError("Number cannot be negative.")
    print(f"{number} is a positive number.")

# Run bit
try:
    check_positive(5)
    check_positive(-1)
except NegativeNumberError as e:
    print(f"Caught an exception: {e}")
finally:
    print("Execution finished.")
