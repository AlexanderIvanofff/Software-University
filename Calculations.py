import operator


def perform_operation(a, b, operation):
    operation_fn = None
    if operation == 'multiply':
        operation_fn = operator.mul

    elif operation == 'divide':
        operation_fn = operator.truediv

    elif operation == 'add':
        operation_fn = operator.add

    elif operation == 'subtract':
        operation_fn = operator.sub
    return operation_fn(a, b)


operations = input()
first_number = int(input())
second_number = int(input())
print(perform_operation(first_number, second_number, operations))