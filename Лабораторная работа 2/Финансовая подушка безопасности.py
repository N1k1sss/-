money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0
money = money_capital + salary

while money >= spend:
    money += salary - spend
    spend = spend + spend * increase
    month += 1

print('Количество месяцев, которое можно протянуть без долгов:', month)
