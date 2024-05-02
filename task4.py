list = input().split()
dicti = {
    'jone':input(),
    'emma':input(),
    'kelly':input(),
    'jason':input(),
}

list2 = []
for i in list:
    for key,val in dicti.items():
        if val == i:
            list2.append(i)
print(list2)
