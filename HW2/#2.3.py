#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и dict.

seasons = {'зимний': (1, 2, 12), 'весенний': (3, 4, 5), 'летний': (6, 7, 8), 'осенний': (9, 10, 11)}
month = int(input("Введите значение текущего месяца в виде целого числа: "))
for key in seasons.keys():
    if month in seasons[key]:
        print(f"Это {key} месяц.")


