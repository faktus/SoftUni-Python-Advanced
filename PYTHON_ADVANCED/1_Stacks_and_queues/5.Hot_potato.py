from collections import deque

group = deque(input().split())
deadly_potato = int(input())
count = 0
flag = False
while True:
    
    for i in list(group):
        count += 1
        if len(group) == 1:
            flag = True
            break
        if count == deadly_potato:
            print(f"Removed {i}")
            group.remove(i)
            count = 0
    if flag:
        break
    
print(f'Last is', ''.join(group))