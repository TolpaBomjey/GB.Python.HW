# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена,
# количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# # [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# # {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

print("Здравствуй, касатик. Будем играть в мерчендазера")
countItems = int(input("Сколько у тебя товаров? >>>"))
items = list()
names = ("название", "цена", "количество", "eд")
analitics = list()
allByName = dict()

for i in range(countItems):
    print(f"Заполняем {i} товар")
    type = input("Что за товар >>>")
    price = int(input("Его цена >>>"))
    count = int(input("Сколько едениц >>>"))
    thing = input("Единица измерения >>>")
    items.append((i + 1, {names[0]: type, names[1]: price, names[2]: count, names[3]: thing}))
    analitics.append([type, price, count, thing])
print("Анализирую....")

print("Ваши товары:")
for q in items:
    print(q, sep="\n")

zipAnalitic = list(zip(*analitics))
for q in range(4):
    allByName.update({names[q]: zipAnalitic[q]})

print("Аналитика товаров:")
for q in allByName.items():
    print(q, sep="\n")
