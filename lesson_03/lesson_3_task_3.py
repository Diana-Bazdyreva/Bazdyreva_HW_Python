from address import Address
from mailing import Mailing

to_address = Address(400002, "Volgograd", "Kurchatova", 14, 198)
from_address = Address(357560, "Pyatigorsk", "Sadovaya", 1, 1)

mailing = Mailing("7548965", from_address, to_address, "550")

print(f"Отправление {mailing.track} из {mailing.from_address.index},"
      f"{mailing.from_address.city}, {mailing.from_address.street},"
      f" {mailing.from_address.house}, {mailing.from_address.flat}, в"
      f" {mailing.to_address.index}, {mailing.to_address.city},"
      f" {mailing.to_address.street}, {mailing.to_address.house},"
      f" {mailing.to_address.flat}. Стоимость: {mailing.cost} рублей")
