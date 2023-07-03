from address import Address
from mailing import Mailing

address_1 = Address("199999", "Санкт-Петербург", "Невский пр.", '58', '55')
address_2 = Address("195178", "Москва", "Красная пл.", "5", "30")
cost_1 = 100
track_1 = 'Петербург - Москва'

mailing_1 = Mailing(address_1, address_1, cost_1, track_1)

print(f'Отправление {mailing_1.track} из {mailing_1.from_address.index}, \
{mailing_1.from_address.city}, {mailing_1.from_address.street}, \
{mailing_1.from_address.house} - {mailing_1.from_address.flat} в \
{mailing_1.to_address.index}, {mailing_1.to_address.city}, \
{mailing_1.to_address.street}, {mailing_1.to_address.house} - \
{mailing_1.to_address.flat}. Стоимость {mailing_1.cost} рублей.')
