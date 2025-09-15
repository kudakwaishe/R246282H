def classify_number():

    while True:
        try:
            num = int(input("Enter an integer: "))
            if num > 0:
                return "Positive"
            elif num < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("Invalid input. Please enter a valid integer.")