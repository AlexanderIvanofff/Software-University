number_room = int(input())
total_free_chairs = 0
has_enough_space = True

for i in range(1, number_room + 1):
    room_data = input().split()
    chairs_count = len(room_data[0])
    numbers_of_seat = int(room_data[1])

    if chairs_count >= numbers_of_seat:
        total_free_chairs += chairs_count - numbers_of_seat
    else:
        has_enough_space = False
        print(f'{numbers_of_seat - chairs_count} more chairs needed in room {i}')

if has_enough_space:
    print(f'Game On, {total_free_chairs} free chairs left')