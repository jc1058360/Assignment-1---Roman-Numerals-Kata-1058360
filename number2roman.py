from converters import convert_number


while True:
    number = abs(int(
        input("Enter a positive number to convert to Roman Numeral > ")))

    if number == 0:
        print("Romans did not have a representation for zero")
    elif number > 0:
        print(
            f"The number {number} converted to Roman Numeral is {convert_number(number)}")
        break
