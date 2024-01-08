def even_odd(*args):
    
    command = args[-1]

    if command == 'even':
        even = [el for el in args if isinstance(el, int) and el % 2 == 0] 
        return even
    elif command  == 'odd':
        odd = [el for el in args if isinstance(el, int) and el % 2 != 0]
        return odd

    
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))