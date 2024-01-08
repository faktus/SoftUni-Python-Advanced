row = int(input())

matrix = []

for _ in range(row):
    numbers = [el for el in input()]
    matrix.append(numbers)

symbol = input()
flag = False
for i in range(row):
    if flag:
        break
    for j in range(row):
        if matrix[i][j] == symbol:
            print(f'({i}, {j})')
            flag = True
            break

if not flag:
    print(f'{symbol} does not occur in the matrix')