n = int(input())

party_guests = set()

while True:
    
    code = input()
    
    if code == 'END':
        break

    if code in party_guests:
        
        party_guests.remove(code)
    
    else:
        
        party_guests.add(code)

sorted_set = sorted(party_guests)

print(len(party_guests))
print('\n'.join(sorted_set))