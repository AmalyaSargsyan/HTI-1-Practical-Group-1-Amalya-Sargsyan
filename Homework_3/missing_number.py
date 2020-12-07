# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի իրարից բացատով առանձնացված N-1 քանակությամբ թվեր,
# որոնք գտնում են [1, N] միջակայքում և չեն կրկնվում։ Դա նշանակում է, որ այդ միջակայքում կա մի թիվ
# որը բացակայում մուտքագրված արժեքի մեջ։ Ծրագիրը պետք է գտնի և տպի այդ թիվը։

def missing_number(numbers):
    numbers = [int(i) for i in numbers.split()]
    numbers.sort()

    if numbers[0] != 1:
        return 1

    if numbers[-1] != len(numbers) + 1:
        return len(numbers) + 1

    for i in range(2, len(numbers)):
        _missing_num = numbers[i - 1] + 1
        if numbers[i] != _missing_num:
            return _missing_num


print(missing_number(input("Enter numbers separated by space: ")))
