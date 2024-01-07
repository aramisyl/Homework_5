bin = input("Введите число в двоичной системе счисления.")
decimal = int(bin, 2)
octal = oct(decimal)
hexidecimal = hex(decimal)

print("Decimal: {}, Octal: {}, Hexadecimal: {}".format(decimal, octal, hexidecimal))
print(f"Decimal: {decimal}, Octal: {octal}, Hexadecimal: {hexidecimal}.")
print("Decimal: %d, Octal: %s, Hexadecimal: %s." % (decimal, octal, hexidecimal))


