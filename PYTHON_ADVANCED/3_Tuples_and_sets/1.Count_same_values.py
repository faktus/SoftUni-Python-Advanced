tuple_of_numbers = tuple(float(x) for x in input().split())
num = []

for i in tuple_of_numbers:
    if i not in num:
        num.append(i)
        counter = tuple_of_numbers.count(i)
        print(i, '-', counter, 'times')