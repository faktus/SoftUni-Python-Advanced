from collections import deque

def refill(liters, quantity):
    return quantity + liters


quantity = int(input())

names = deque([])

while True:
    name = input()

    if name == 'Start':
        break
    names.append(name)

while True:
    command = input().split()
    if 'End' in command:
        print(f'{quantity} liters left')
        break


    if 'refill' in command:
        quantity = refill(int(command[1]), quantity)
    elif quantity >= int(command[0]):
        print(f'{names.popleft()} got water')
        quantity -= int(command[0])
    else:
        print(f'{names.popleft()} must wait')
    