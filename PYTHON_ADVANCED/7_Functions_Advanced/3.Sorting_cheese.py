def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cheese, quantity in sorted_cheese:
        result += f'{cheese}\n'
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join([str(el) for el in sorted_quantity])
        result += '\n'
    return result
    

print(sorting_cheeses(Parmesan=[102, 120], Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125],))