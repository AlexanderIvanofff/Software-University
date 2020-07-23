price_vacation = float(input())
count_puzzle = int(input())
count_dolls = int(input())
count_beers = int(input())
count_minions = int(input())
count_trucks = int(input())

puzzle = 2.6
dolls = 3
beers = 4.1
minion = 8.2
trucks = 2

price_toys = count_puzzle * puzzle + count_dolls * dolls + count_beers * beers\
    + count_minions * minion + count_trucks * trucks

number_toys = count_puzzle + count_dolls + count_beers + count_minions + count_trucks


if number_toys >= 50:
    price_toys *= 0.75

rent = price_toys / 10
final_price = price_toys - rent

if final_price >= price_vacation:
    money_left = abs(price_vacation - final_price)
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_need = abs(final_price - price_vacation)
    print(f'Not enough money! {money_need:.2f} lv needed.')






