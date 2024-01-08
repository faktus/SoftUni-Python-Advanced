n = int(input())
names = []

for _ in range(n):
    names.append(input())

print('\n'.join(set(names)))