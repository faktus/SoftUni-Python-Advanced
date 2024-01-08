n = int(input())

longest_intersection = []
intersections = []

for _ in range(n):

    first_set, second_set = input().split('-')
    
    first_set = [int(x) for x in first_set.split(',')]
    second_set = [int(x) for x in second_set.split(',')]
    

    intersections.append({x for x in range(first_set[0], first_set[1] + 1)}.intersection({x for x in range(second_set[0], second_set[1] + 1)}))
    longest_intersection.append(len({x for x in range(first_set[0], first_set[1] + 1)}.intersection({x for x in range(second_set[0], second_set[1] + 1)})))

maximum = max(longest_intersection)

for i in intersections:
    if len(i) == maximum:
        print(f'Longest intersection is {list(i)} with length {maximum}')

