from math import pi

figures = input()

if figures == 'square':
    side = float(input())
    area = side * side

elif figures == 'rectangle':
    length_A = float(input())
    length_B = float(input())
    area = length_A * length_B

elif figures == 'circle':
    radius = float(input())
    area = pi * radius ** 2

elif figures == 'triangle':
    length = float(input())
    width = float(input())
    area =  length * width / 2

print(f'{area:.3f}')





