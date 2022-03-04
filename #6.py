#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
#Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
day = 1
start_dist = float(input("Enter amount of km for the Day1: "))
finish_dist = float(input("Enter amount of km for the Last Day: "))

while start_dist < finish_dist:
        start_dist = start_dist + start_dist * 0.1
        day += 1
print(f"Sportsman would achieve his result on day {day}.")






