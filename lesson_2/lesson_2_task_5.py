def month_to_season(month_num):
    if month_num == 12 or 1 <= month_num <= 2:
        print('Зима')
    elif 3 <= month_num <= 5:
        print('Весна')
    elif 6 <= month_num <= 8:
        print('Лето')
    elif 9 <= month_num <= 11:
        print('Осень')
    else:
        print('Некорректный номер')


month_to_season(int(input()))
