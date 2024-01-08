def movement(hz):
    if 0 <= current_col < rows and 0 <= current_row < rows:
        if field[current_row][current_col] == 't':
            return 'trap'
        elif field[current_row][current_col] == 'h':
            return 1       
    else:
        return 'out'

rows = int(input())
moves = input().split(', ')
field = [[place for place in input()] for _ in range(rows)]

for row in range(len(field)):
    if 's' in field[row]:
        current_row = row
        current_col = field[row].index('s')
        break

hazelnuts = 0

for move in moves:
    
    if move == 'down':
        current_row += 1
        result = movement(hazelnuts)
    elif move == 'up':
        current_row -= 1
        result = movement(hazelnuts)
    elif move == 'right':
        current_col += 1
        result = movement(hazelnuts)
    elif move == 'left':
        current_col -= 1
        result = movement(hazelnuts)
    if type(result) == int:
        hazelnuts += 1
    if result == 'out':
        print("The squirrel is out of the field.")
        break
    if result == 'trap':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
elif result != 'out' and result != 'trap':
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")