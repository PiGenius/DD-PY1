money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money_capital -= spend
while money_capital >= 0:
    spend *= (1 + increase)
    money_capital += salary - spend
    month += 1

print(month)
