lines = input().split()

row = int(lines[0])
col = int(lines[1])

matrix = [[el for el in input().split()] for _ in range(row)]

count = 0

for i in range(row - 1):
    
    for j in range(col - 1):

        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:

            count += 1

print(count)