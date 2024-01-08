N, M = [int(num) for num in input().split(',')]

board = [[place for place in input()] for _ in range(N)]

cheese = 0

for row in range(len(board)):
    if 'M' in board[row]:
        mouse_ROW = row
        mouse_COL = board[row].index('M')
    if 'C' in board[row]:
        cheese += board[row].count('C')

command = ''

while command != 'danger' and cheese != 0:
    
    command = input()
    symbol = ''

    if command == 'down':
        if mouse_ROW + 1 < N:        
            if board[mouse_ROW + 1][mouse_COL] != '@':
                
                board[mouse_ROW][mouse_COL] = '*'
                mouse_ROW += 1
                symbol = board[mouse_ROW][mouse_COL]
                board[mouse_ROW][mouse_COL] = 'M'
        else:
            print('No more cheese for tonight!')
            break

    elif command == 'up':
        if mouse_ROW - 1 >= 0:        
            if board[mouse_ROW - 1][mouse_COL] != '@':
                
                board[mouse_ROW][mouse_COL] = '*'
                mouse_ROW -= 1
                symbol = board[mouse_ROW][mouse_COL]
                board[mouse_ROW][mouse_COL] = 'M'
        else:
            print('No more cheese for tonight')
            break

    elif command == 'right':
        if mouse_COL + 1 < M:        
            if board[mouse_ROW][mouse_COL + 1] != '@':
                
                board[mouse_ROW][mouse_COL] = '*'
                mouse_COL += 1
                symbol = board[mouse_ROW][mouse_COL]
                board[mouse_ROW][mouse_COL] = 'M'
        else:
            print('No more cheese for tonight')
            break

    elif command == 'left':
        if mouse_COL - 1 >= 0:        
            if board[mouse_ROW][mouse_COL - 1] != '@':
                
                board[mouse_ROW][mouse_COL] = '*'
                mouse_COL -= 1
                symbol = board[mouse_ROW][mouse_COL]
                board[mouse_ROW][mouse_COL] = 'M'
        else:
            print('No more cheese for tonight!')
            break 
        
    if symbol == 'T':
        print('Mouse is trapped!')
        break
    if symbol == 'C':
        cheese -= 1

if cheese == 0:
    print('Happy mouse! All the cheese is eaten, good night!')
elif command == 'danger':
    print('Mouse will come back later!')

for i in board:
    print(''.join(i))