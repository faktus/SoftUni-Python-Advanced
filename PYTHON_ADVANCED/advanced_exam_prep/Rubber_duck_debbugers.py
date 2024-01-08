from collections import deque

time = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

darth_vader_ducky = 0
thor_ducky = 0
bbrd = 0
sYrD = 0

while time:
    current_time = time.popleft()
    current_task = tasks.pop()

    if current_task * current_time > 240:
        current_task -= 2
        time.append(current_time)
        tasks.append(current_task)
        continue
    
    current_ducky = current_task * current_time

    if current_ducky <= 60:
        darth_vader_ducky += 1
    elif current_ducky <= 120:
        thor_ducky += 1
    elif current_ducky <= 180:
        bbrd += 1
    else:
        sYrD += 1


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky}\nThor Ducky: {thor_ducky}\nBig Blue Rubber Ducky: {bbrd}\nSmall Yellow Rubber Ducky: {sYrD}")
