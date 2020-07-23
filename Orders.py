def product(p, c):
    price = None
    if p == 'coffee':
        price = 1.50
    elif p == 'water':
        price = 1.00
    elif p == 'coke':
        price = 1.40
    elif p == 'snacks':
        price = 2.00
    if price is not None:
        return price * c


first_product = input()
count_product = float(input())

print(f'{product(first_product, count_product):.2f}')
