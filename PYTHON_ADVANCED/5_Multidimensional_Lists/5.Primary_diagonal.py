row = int(input())

matrix = []
primary_diagonal = 0

for i in range(row):
    numbers = [int(el) for el in input().split()]
    matrix.append(numbers)
    primary_diagonal += matrix[i][i]

print(primary_diagonal)