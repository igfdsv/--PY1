salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def capital_required_for(months, salary, spend, increase = 0.03):
    result = 0
    for m in range(months):
        result += spend - salary
        spend += spend * increase
    return result

need_money = capital_required_for(months, salary, spend, increase)

print(round(need_money))
