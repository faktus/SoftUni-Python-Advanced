command = input().split(', ')

row = int(command[0])
col = int(command[1])

matrix = []

sum_num = 0

for _ in range(row):
    numbers = [int(i) for i in input().split(', ')]
    sum_num += sum(numbers)
    matrix.append(numbers)

print(sum_num)
print(matrix)