while True:
    try:
        number = int(input("Enter a number: "))
        print(f"You entered the valid number: {number}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")