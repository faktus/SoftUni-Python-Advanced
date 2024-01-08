def age_assignment(*args, **kwargs):

    new_dict = {}
    

    for key, value in kwargs.items():

        for name in args:

            if key == name[0]:
                new_dict[name] = value
    
    sorted_dict = sorted(new_dict.items(), key=lambda x: x[0])

    return '\n'.join([f'{name} is {age} years old.' for name, age in sorted_dict])


print(age_assignment("Peter", "George", G=26, P=19))