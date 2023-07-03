def square(side):
    s = side**2
    if (s % 1 != 0):
        s = s//1 + 1
    return int(s)


print(square(float(input('Введите число: '))))
