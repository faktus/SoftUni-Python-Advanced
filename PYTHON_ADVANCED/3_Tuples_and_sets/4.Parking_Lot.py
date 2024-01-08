n = int(input())

parking_lot = set()

for _ in range(n):
    
    direction, license_plate = input().split(", ")

    if direction == 'IN':
        
        parking_lot.add(license_plate)
    
    elif direction == "OUT":
        
        parking_lot.remove(license_plate)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")