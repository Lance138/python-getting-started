def get_input():
        number = input("enter a number: ")
        try:
            number = float(number)
            return number
        except ValueError:
            print("Invalid input.")
            return None
        
def check_number(number):
    if number.is_integer():
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    else:
        print("That is not a whole number!")

def main():
    number = get_input()
    if number is not None:
         check_number(number)
main()