n = int(input())
count = 0

odd_set = set()
even_set = set()

for _ in range(n):
    
    count += 1
    
    name = sum([ord(x) for x in input()]) // count
    
    if name % 2 == 0:
        even_set.add(name)
    else:
        odd_set.add(name)


if sum(odd_set) == sum(even_set):
    
    print(', '.join({str(x) for x in even_set}), end=', ')
    print(', '.join({str(x) for x in odd_set}))

elif sum(odd_set) > sum(even_set):

    print(', '.join({str(x) for x in odd_set.difference(even_set)}))

else:

    print(', '.join(str(x) for x in odd_set.symmetric_difference(even_set)))

