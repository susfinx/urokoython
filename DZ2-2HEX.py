def decimal_to_hexadecimal(decimal):
    hex_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16

        if remainder > 9:
            remainder = hex_dict[remainder]

        hexadecimal = str(remainder) + hexadecimal
        decimal = decimal // 16

    return hexadecimal

decimal_number = int(input("Введите целое число: "))

hexadecimal_number = decimal_to_hexadecimal(decimal_number)

print("Шестнадцатеричное представление числа:", hexadecimal_number)

hex_check = hex(decimal_number)[2:]

print("Шестнадцатеричное представление числа:", hex_check)
