line = input().split()

row = int(line[0])
col = int(line[1])

matrix = [[int(el) for el in input().split()] for _ in range(row)]

matrix_sum = []

for j in range(row - 2):

    for i in range(col - 2):
        var = []
        for reda in range(3):      # 3x3 box

            for kolonata in range(3):

                var.append(matrix[j + reda][kolonata + i])

        var.append(sum(var))

        if matrix_sum:
            if sum(matrix_sum[0]) < sum(var):
                matrix_sum[0] = var
        else:

            matrix_sum.append(var)

print(f"Sum = {matrix_sum[0].pop()}")

for _ in range(3):
    var = []
    for _ in range(3):
        var.append(matrix_sum[0].pop(0))
        
    print(*var)
    