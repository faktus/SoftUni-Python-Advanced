line = input().split(', ')

row = int(line[0])
col = int(line[1])

matrix = []

for _ in range(row):
    numbers = [int(el) for el in input().split()]
    matrix.append(numbers)
 


for i in range(col):
    sum_col = 0
    for j in range(row):
        sum_col += matrix[j][i]
        
    print(sum_col)