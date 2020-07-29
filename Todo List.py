tasks = []

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    priority = tokens[0]
    note = tokens[1]
    tasks.append((priority, note))

sorted_task = [task_name for priority, task_name in sorted(tasks)]
print(sorted_task)