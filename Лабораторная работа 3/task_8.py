money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def enough_for(capital, salary, spend, increase = 0.05):
    month = 0
    while True:
        capital -= spend - salary
        spend += spend * increase
        month += 1
        if capital < 0:
            return month - 1

month = enough_for(money_capital, salary, spend, increase)

print(month)
