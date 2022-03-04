#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = (input("Enter any number from 1 to 9: "))
a = n + n
b = n + n + n
answer = int(n) + int(a) + int(b)
print(f"{n} + {n}{n} + {n}{n}{n} = {answer}")
