row = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(row)]

Primary_diagonal = [matrix[i][i] for i in range(row)]
secondary_diagonal = [matrix[i][row - i - 1] for i in range(row)]

print(f'Primary diagonal: {", ".join([str(el) for el in Primary_diagonal])}. Sum: {sum(Primary_diagonal)}')

print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')

