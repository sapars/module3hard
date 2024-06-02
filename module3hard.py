# Дополнительное практическое задание по модулю: "Подробнее о функциях."
'''

Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99
'''

def cals_str_sum( *args):
    sum = 0
    for i in args:
        if isinstance(i, int):
            sum += i
            continue
        if isinstance(i, float):
            sum += i
            continue
        if isinstance(i, str):
            sum += len(i)
            continue
        if isinstance(i, tuple):
            sum += cals_str_sum(*i)
        if isinstance(i, list):
            sum += cals_str_sum(*i)
        if isinstance(i, dict):
            sum += cals_str_sum(*i.items())
        if isinstance(i, set):
            sum += cals_str_sum(*i)
    return sum


data_structure = [
   [1, 2, 3],
   {'a': 4, 'b': 5},
   (6, {'cube': 7, 'drum': 8}),
   "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]


print(cals_str_sum(data_structure))
