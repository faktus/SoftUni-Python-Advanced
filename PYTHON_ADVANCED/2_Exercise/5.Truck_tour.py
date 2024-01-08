from collections import deque

gas_stations = int(input())
pump = deque()

start_position = 0
stops = 0
fuel = 0

for _ in range(gas_stations):
    
    pump.append([int(x) for x in input().split()])


while stops < gas_stations:

    fuel = 0

    for i in range(gas_stations):
        
        fuel += pump[i][0]
        distance = pump[i][1]
        
        if fuel - distance >= 0:
            fuel -= distance
            stops += 1

        else:
            stops = 0
            start_position += 1
            pump.rotate(-1)
            break

print(start_position)