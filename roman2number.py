from converters import convert_symbol


while True:
    symbol = input("Enter a Roman Numeral to convert to number > ")
    print(
        f"The symbol {symbol.upper()} is equivalent to the number {convert_symbol(symbol.upper())}")
    break
