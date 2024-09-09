data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    summa = 0
    if type(data_structure) is float:
        summa += data_structure
    if type(data_structure) is int:
        summa += data_structure
    elif type(data_structure) is str:
        summa += len(data_structure)
    elif type(data_structure) is list:
        for i in data_structure:
            summa += calculate_structure_sum(i)
    elif type(data_structure) is tuple:
        for i in data_structure:
            summa += calculate_structure_sum(i)
    elif type(data_structure) is set:
        for i in data_structure:
            summa += calculate_structure_sum(i)
    elif type(data_structure) is dict:
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)

    return summa


result = calculate_structure_sum(data_structure)
print(result)
