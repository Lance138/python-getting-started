number = input("Enter a number:")
try:
    number = float(number)
    if number.is_integer():
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    else:
        print("That is not a whole number!")
except ValueError:
    print("Invalid input")