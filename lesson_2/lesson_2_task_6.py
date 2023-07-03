lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


def filter(list):
    for i in range(len(list)):
        if list[i] < 30 and list[i] % 3 == 0:
            print(list[i])


filter(lst)
