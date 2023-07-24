def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        argument_dict[str(value)] = key
    return argument_dict

arguments_dict = create_argument_dict(a=10, b="hello", c=[1, 2, 3])
print(arguments_dict)
