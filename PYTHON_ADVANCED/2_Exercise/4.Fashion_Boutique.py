cloths_as_stack = list(map(int, input().split()))
capacity_of_rack = int(input())

one_rack = capacity_of_rack
count = 1

while cloths_as_stack:

    if one_rack >= cloths_as_stack[-1]:
    
        one_rack -= cloths_as_stack.pop()
    
    else:
        
        count += 1
        one_rack = capacity_of_rack

print(count)