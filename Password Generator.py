n = int(input())
currnet = 1
is_currnet_bigger = False

for a in range(1, n + 1):
    for b in range(1, a + 1):

        if currnet > n:
            is_currnet_bigger = True
            break
        print(f'{currnet}' + ' ', end='')
        currnet += 1
    if is_currnet_bigger:
        break
    print()