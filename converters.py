numerals = {"I": 1, 'IV': 4, "V": 5, 'IX': 9, "X": 10, 'XL': 40,
            "L": 50, 'XC': 90, "C": 100, 'CD': 400, "D": 500, 'CM': 900, "M": 1000}


def convert_number(input_number):
    scope = None
    for symbol, integer in numerals.items():
        if integer == input_number:
            return symbol
        if input_number > integer:
            scope = symbol

    remaining = input_number - numerals[scope]
    return scope + convert_number(remaining)


def convert_symbol(symbol):
    i = 0
    num = 0
    while i < len(symbol):
        if i + 1 < len(symbol) and symbol[i:i+2] in numerals:
            num += numerals[symbol[i:i+2]]
            i += 2
        else:
            num += numerals[symbol[i]]
            i += 1
    return num
