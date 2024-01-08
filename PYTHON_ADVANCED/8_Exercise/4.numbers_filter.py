def even_odd_filter(**kwargs):

    for keys, values in kwargs.items():
        if keys == 'even':  

            kwargs[keys] = [el for el in values if el % 2 == 0]

        elif keys == 'odd':

            kwargs[keys]  = [el for el in values if el % 2 != 0]
    
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))