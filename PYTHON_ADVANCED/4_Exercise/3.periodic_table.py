n = int(input())

unique_chemicals = set()

for _ in range(n):

    chemicals = input().split()

    for x in range(len(chemicals)):
        unique_chemicals.add(chemicals[x])

print('\n'.join([str(x) for x in unique_chemicals]))