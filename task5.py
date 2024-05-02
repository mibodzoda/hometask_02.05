dict = {'jan': 47,
        'feb': 52,
        'march': 47,
        'april': 44,
        'may': 52,
        'june': 53,
        'july': 55,
        'august': 54,
        'september': 56,
        'october': 47,
        'november': 44,
        'december': 53
}

list1 = []
for value in dict.values():
    list1.append(value)
print(list(set(list1)))