row = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(row)]

primary_diagonal = [matrix[i][i] for i in range(row)]
secondary_diagonal = [matrix[i][row - i - 1] for i in range(row)]

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)