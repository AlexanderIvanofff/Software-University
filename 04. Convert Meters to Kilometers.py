import sys


n = int(input())
max_value = -sys.maxsiz
max_snow = 0
max_time = 0
max_quality = 0

for i in range(n):
    snow_ball_Snow = int(input())
    snow_ball_Time = int(input())
    snow_ball_Quality = int(input())

    value = (snow_ball_Snow // snow_ball_Time) ** snow_ball_Quality

    if value > max_value:
        max_value = value
        max_snow = snow_ball_Snow
        max_time = snow_ball_Time
        max_quality = snow_ball_Quality

print(f'{max_snow} : {max_time} = {max_value} ({max_quality})')


