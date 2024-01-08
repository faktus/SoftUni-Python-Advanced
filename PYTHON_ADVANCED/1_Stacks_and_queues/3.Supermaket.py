from collections import deque

clients = deque([])

while True:
    
    new_client = input()
    
    if new_client == 'End':
        break
    elif new_client == 'Paid':
        while clients:
            print(clients.popleft())
            
        continue 
    clients.append(new_client)

print(f"{len(clients)} people remaining.")