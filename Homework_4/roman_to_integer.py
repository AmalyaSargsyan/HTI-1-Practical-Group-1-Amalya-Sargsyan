# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի հռոմեական թիվ և ծրագիրը կտպի այն ամբողջ թվի տեսքով։

def roman_to_integer(value):
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    value = value.replace("IV", "IIII")
    value = value.replace("IX", "VIIII")
    value = value.replace("XL", "XXXX")
    value = value.replace("XC", "LXXXX")
    value = value.replace("CD", "CCCC")
    value = value.replace("CM", "DCCCC")

    for i in value:
        num += roman_numbers[i]

    print(num)
    return num


roman_to_integer(input())
