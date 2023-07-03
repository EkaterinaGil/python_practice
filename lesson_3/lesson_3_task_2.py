from smartphone import Smartphone

item_1 = Smartphone('Apple', 'iPhone 12', '+79002003030')
item_2 = Smartphone('Apple', 'iPhone SE', '+79995504444')
item_3 = Smartphone('Xiaomi', 'Redmi 9C', '+79667878999')
item_4 = Smartphone('HONOR', 'X8', '+79679905454')
item_5 = Smartphone('Samsung', 'Galaxy A03', '+79858765231')

catalog = [item_1, item_2, item_3, item_4, item_5]

for value in catalog:
    print(f"{value.label} - {value.model}. {value.phone_number}")
