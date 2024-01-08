def concatenate(*args, **kwargs):
    result = ''.join(args)
    result = [let for let in result]

    for key, value in kwargs.items():
        if key[0] in result:
            index = result.index[key[0]]

            for let in range(index, index + len([let for let in value])):
                result.remove(let)