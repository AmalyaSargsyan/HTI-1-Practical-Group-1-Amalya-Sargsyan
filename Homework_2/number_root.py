def number_root(num):
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10

    if sum_of_digits > 9:
        return number_root(sum_of_digits)
    return sum_of_digits


print(number_root(int(input("Enter a number: "))))

