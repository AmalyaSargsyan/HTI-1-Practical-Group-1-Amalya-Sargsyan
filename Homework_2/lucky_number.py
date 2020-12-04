# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի թիվ և ծրագիրը կտպի Yes եթե թիվը հաջողակ է և No հակառակ դեպքում։
# Հաջողակ կհամարվի այն թիվը, որի կենտ (odd) ինդեքսում գտնվող նիշերը գումարը հավասար կլինի
# զույգ (even) ինդեքսում գտնվող նիշերի գումարին։

def lucky_number(num):
    sum_of_even_digits, sum_of_odd_digits = 0, 0
    for i in range(0, len(num), 2):
        sum_of_even_digits += int(num[i])
    for i in range(1, len(num), 2):
        sum_of_odd_digits += int(num[i])
    if sum_of_even_digits == sum_of_odd_digits:
        return "Yes"
    return "No"


print(lucky_number(input("Enter a number: ")))
