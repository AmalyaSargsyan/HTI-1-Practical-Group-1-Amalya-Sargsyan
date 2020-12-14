# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի տեքստ և ծրագիրը կտպի տեքստում առկա բոլոր նիշերը և իրենց քանակները։
# (Լուծման մեջ օգտագործել dict)

text = list(input())

char_count = {}
for i in range(0, len(text)):
    char = text[i]
    count = text.count(text[i])
    _ = {char: count}
    char_count.update(_)
print(char_count)


