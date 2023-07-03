def is_year_leap(year):
    if year % 4 == 0:
        return "True"
    else:
        return "False"


year = input("Введите год: ")
res = is_year_leap(int(year))

print(f"год {year}: {res}")
