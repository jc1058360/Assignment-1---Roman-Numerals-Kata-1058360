import converters
# Zeros and negative numbers are handled in number2roman.py
print(converters.convert_number(17))
print(converters.convert_number(4))
print(converters.convert_number(1000))
print(converters.convert_number(765))
print(f'\n')
# Lowercase letters are handled in roman2number.py
print(converters.convert_symbol("IV"))
print(converters.convert_symbol("CC"))
print(converters.convert_symbol("DCCLXV"))
# This test is an invalid Roman Numeral
print(converters.convert_symbol("IIII"))
