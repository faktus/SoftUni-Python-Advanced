n = int(input())
queries = []

for i in range(n):
    command = input().split()
    if command[0] == '1':
        queries.append(int(command[1]))
    elif queries:
        if command[0] == '2':       
            queries.pop()
        elif command[0] == '3':
            print(max(queries))
        elif command[0] == '4':
            print(min(queries)) 


while queries:
    print(queries.pop(), end='')
    if queries:
        print(', ', end='')