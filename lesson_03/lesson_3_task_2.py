from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphone_15", "+79033735641"),
    Smartphone("Apple", "iphone_16", "+79000000000"),
    Smartphone("Nokia", "3310", "+79011111111"),
    Smartphone("Samsung", "SGH-210", "+79022222222"),
    Smartphone("Motorola", "M3688", "+79033333333")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
