#*Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя
# Пример готовой структуры:
# [
#  (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
#}


inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break

    i += 1

print(f'список товаров:{inventory_tuple_list}')

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'собрана аналитика: {output_dict}')
