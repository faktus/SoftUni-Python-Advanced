lines = input().split(', ')

row = int(lines[0])
col = int(lines[1])

matrix = []

for _ in range(row):
    numbers = [int(el) for el in input().split(', ')]
    matrix.append(numbers)

group = []
i = 0
j = 0

while True:

    sum_of_square = 0
    square = []
    
    if j + 1 == col:
        j = 0
        i += 1
    if i + 1 == row:
        break
    

    sum_of_square += matrix[i][j] + matrix[i][j + 1] + matrix[i+1][j] + matrix[i+1][j+1]
    
    square.append(matrix[i][j])
    square.append(matrix[i][j + 1])
    square.append(matrix[i+1][j])
    square.append(matrix[i+1][j+1])
    square.append(sum_of_square)

    group.append(square)


    j += 1
max_group = max(group)

c = 0

for i in max_group:
    c += 1
    print(i, end=' ')
    if c == 2:
        c = 0
        print()
    
