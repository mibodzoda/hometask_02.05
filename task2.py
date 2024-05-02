list = input().split()
chunk = 3
for i in range(0,len(list),chunk):
    res = list[i: i+chunk]
    print(res[::-1])