def bank(X, Y):
    for i in range(Y):
        X += X*0.1
    print("Искомая сумма: ", round(X, 2))


a = float(input("Введите сумму вклада: "))
b = int(input("Введите срок вклада (лет): "))
bank(a, b)
