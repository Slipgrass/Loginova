#*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#Каждый кортеж хранит информацию об отдельном товаре.
#В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
#название, цена, количество, единица измерения.
#Структуру нужно сформировать программно, запросив все данные у пользователя.
#
#Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
#характеристика товара, например, название.
#Тогда значение — список значений-характеристик, например, список названий товаров.
list_of_items = []
num = 1
item = {}
data_collection = True
while data_collection:
    item["name"] = input("\nType the name of the equipment: ")
    item["price"] = input("\nWhat is the price of the equipment: ")
    item["ammount"] = input("\nHow many items of this equipment: ")
    item["units"] = input("\nWhat are the units of measurement: ")
    list_of_items.append((num, item.copy()))
    num += 1
    repeat = input("\nWould you like to enter mor data? yes/no ")
    if repeat == "no":
        data_collection = False

for k, v in list_of_items():
    print(f"{k} - {v}")


#понимаю, что фигня получилась

