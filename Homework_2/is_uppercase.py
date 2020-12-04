# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի տեքստ և
# ծրագիրը կտպի Yes եթե մուտքագրված տեքստում բոլոր տառերը մեծատառ են և No հակառակ դեպքում։

def is_uppercase(word):
    if word.isupper():
        return "Yes"
    return "No"


print(is_uppercase(input("Enter a word: ")))
