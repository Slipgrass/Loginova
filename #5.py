#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма.
#Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#Выведите соответствующее сообщение.

#Если фирма отработала с прибылью, вычислите рентабельность выручки.
#Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
#и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input("Enter your revenue here: "))
expenses = int(input("Enter your expenses here: "))

fin_result = revenue - expenses
if fin_result > 0:
    print ("Congratulations! Your company have finished the financial period with profit.")
    profit_margine = revenue / fin_result * 100
    print(f"Your profitability is {profit_margine:.2f} %.")
    employees = int(input("How many employees do you have: "))
    profit_empl = fin_result // employees
    print(f"Your profit per employee is {profit_empl:.2f}.")
elif fin_result == 0:
    print ("Your company have finished the financial period without profit.")
else:
    print ("Sorry! Your company have finished the financial period with loss.")




