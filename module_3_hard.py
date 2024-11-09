# Дополнительное практическое задание по модулю: "Подробнее о функциях."
#
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются
# в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее,
# даже после сна, его код остался рабочим и выглядел следующим образом:
#
#data_structure = [
#  [1, 2, 3],
#  {'a': 4, 'b': 5},
#  (6, {'cube': 7, 'drum': 8}),
#  "Hello",
#  ((), [{(2, 'Urban', ('Urban2', 35))}])
#]
#
#Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин
# всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#
#Что должно быть подсчитано:
# 1. Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# 2. Все строки (не важно, являются они ключами или значениям или ещё чем-то).


def calculate_structure_sum(data_structure):
    summ = 0
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summ += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        summ += data_structure
    elif isinstance(data_structure, str):
        summ += len(data_structure)
    return summ


result = calculate_structure_sum(data_structure)
print(result)

