#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

n = int(input("Enter any positive integer number: "))
digit_min = 0

while n > 0:
    a = n % 10
    if a > digit_min:
        digit_min = a
        if a == 9:
            break
    n = n // 10
print(f"The biggest digit in your number is {a}")



