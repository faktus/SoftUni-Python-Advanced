row = int(input())

matrix = []

for _ in range(row):
    even_number = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(even_number)

print(matrix)