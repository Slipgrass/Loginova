# вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
print(f"Итого, в приступе прокрастинации вы провели {hours:02}:{minutes:02}:{seconds:02}."
      f"\nНе забудьте, что скоро дедлайн по предоставлению проекта.")







