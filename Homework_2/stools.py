# Ստեղծել ծրագիր, որի միջոցով օգտագործողը կմուտքագրի իրարից բացատով առանձնացված թվեր,
# որոնք դասարանում աշակերտների հասակներն են։ Աշակերտները, բացի ամենաբարձրահասակներից,
# պետք է կանգնեն տարբեր բարձրության աթոռների վրա այնպես, որ արդյունքում բոլորը լինեն նույն հասակի։
# Ծրագիրը պետք է տպի աթոռների բարձրությունների գումարը։

def sum_of_stool_heights(heights):
    heights = [int(i) for i in heights.split()]
    sum1 = 0
    for i in range(len(heights)):
        sum1 += max(heights) - heights[i]
    return sum1


print(sum_of_stool_heights(input("Enter heights separated by space: ")))
