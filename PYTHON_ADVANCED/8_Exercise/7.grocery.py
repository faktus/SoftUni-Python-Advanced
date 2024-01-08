def grocery_store(**kwargs):

    result = []

    sorted_groceries = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for key, value in sorted_groceries:
        result.append(f'{key}: {value}')

    return '\n'.join(result)

print(grocery_store(bread=5,pasta=12, eggs=12,))