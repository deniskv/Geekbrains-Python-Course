# lesson 4 task 4

"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

source_list = [1, 1, 2, 2, 33, 44, 3, 22, 12, 2, 32, 22, 33, 44]
my_new_list = [i for i in source_list if source_list.count(i) < 2]
print(my_new_list)