from collections import deque

quantity = int(input())
food = deque(input().split())

print(max(list(map(int, food))))

while True:
    
    if food:
        
        if quantity >= int(food[0]):

            quantity -= int(food.popleft())
            
        else:
            print("Orders left:", ' '.join(food))
            break
    else:
        print("Orders complete")
        break
