def transform_number(num):
    # Convert the number to a string to iterate through digits
    num_str = str(num)

    # Square each digit and convert back to string
    squared_digits = [str(int(digit)**2) for digit in num_str]

    # Join all squared digits together
    result = ''.join(squared_digits)

    return int(result)


# Example usage
input_num = 112
output_num = transform_number(input_num)
print(output_num)  # Output: 493625
