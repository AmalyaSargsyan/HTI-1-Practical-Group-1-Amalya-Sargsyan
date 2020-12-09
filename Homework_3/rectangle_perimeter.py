# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի ուղղանկյան անկյունների կոորդինատները
# (x1, y1, x2, y2, x3, y3, x4, y4) որպես իրական թվեր և ծրագիրը կտպի ուղղանկյան պարագիծը։
# Ստեղծել և լուծման մեջ օգտագործել segment_length անունով ֆունկցիա, որը կստանա x1, y1, x2, y2 արգումենտներ
# և կվերադարձնի նշված ծայրերով կողմի երկարությունը։

def segment_length(x1, y1, x2, y2):
    if x1 == x2:
        return y2 - y1
    elif y1 == y2:
        return x2 - x1


coordinates = [float(i) for i in input().split()]
length = coordinates[0:4]
width = coordinates[2:6]
perimeter = 2 * (segment_length(*length) + segment_length(*width))
print(perimeter)
