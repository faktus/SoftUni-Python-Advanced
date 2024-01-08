
def top_side():
    for row in range(1, n + 1):
        print(' ' * (n - row), end='')
        print(*['*'] * row)


def bottom_side():
    for row in range(1, n):
        print(' ' * row, end='')
        print(*['*'] * (n - row)) 

        
def rhoumbus():
    top_side()
    bottom_side()

n = int(input())
rhoumbus()


