list1 = input().split()
list2 = input().split()
list3 = []

for i in range(len(list1)):
    if int(i)%2 != 0:
        list3.append(list1[i])

for i in range(len(list2)):
    if int(i)%2 != 0:
        list3.append(list2[i])

print(list3) 