# Գոլդբախի ենթադրությունը նշում է, որ ցանկացած 2-ից մեծ զույգ թիվ կարելի է ներկայացնել որպես 2 պարզ թվերի գումար։
# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի 2-ից մեծ զույգ թիվ և ծրագիրը կտպի 2 պարզ թիվ,
# որոնց գումարը հավասար կլինի մուտքագրված թվին։

def is_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
        else:
            return True


num1 = int(input("Enter an even number greater than 2: "))
if num1 > 2 and num1 % 2 == 0:
    for j in range(2, num1):
        if is_prime(j):
            num2 = num1 - j
            if is_prime(num2):
                print(j, num2)
                break
