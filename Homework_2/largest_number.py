# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի թիվ և ծրագիրը կտպի Yes եթե թվի նիշերը տեղաշարժելով հնարավոր է
# ստանալ մուտքագրված թվից ավելի մեծ թիվ և No հակառակ դեպքում։

def is_larger_number(num):
    num1 = sorted(num, reverse=True)  # մուտքագրված թվի թվանշանները սորտավորել ըստ նվազման
    largest_number = None
    temp = [str(i) for i in num1]
    largest_number = int("".join(temp))  # նվազման կարգով դասավորված list-ը դարձնել int
    num = int("".join(num))  # մուտքագրված թիվը (list տեսակի էր) դարձնել int
    if largest_number > num:
        return "Yes"
    return "No"


print(is_larger_number(list(input("Enter a number: "))))
