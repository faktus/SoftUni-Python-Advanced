numbers = [int(x) for x in input().split()]

number_to_get = int(input())
unique_combinations = ()

for first_number in numbers:

    for second_number in numbers:

        if second_number == first_number:
            continue
        
        if first_number + second_number == number_to_get:
            
            print(f"{first_number} + {second_number} = {number_to_get}")
        
            numbers.remove(second_number)
            
            