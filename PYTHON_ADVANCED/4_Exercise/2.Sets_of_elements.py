n = [int(x) for x in input().split()]

first_set = set()
second_set = set()

count = 0

for _ in range(sum(n)):
    
    number = int(input())

    count += 1

    if count <= n[0]:
        first_set.add(number)
    else:
        second_set.add(number)

print('\n'.join([str(x) for x in first_set.intersection(second_set)]))