from collections import deque

parantheses = deque(input())

opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0

while parantheses or counter < len(parantheses) / 2:
    
    if parantheses[0] in closing_brackets:
    
        break
    
    if parantheses[0] in opening_brackets:
                
        index = opening_brackets.index(parantheses[0])


        if closing_brackets[index] == parantheses[1]:

            parantheses.popleft()
            parantheses.popleft()
            parantheses.rotate(counter)
            counter = 0
            continue

        

        parantheses.rotate(-1)
        counter += 1

if parantheses:
    print('NO')
else:
    print('YES')