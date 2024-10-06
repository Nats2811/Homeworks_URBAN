# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# 1. Название объекта добавлялось в список cls.houses_history.
# 2. Название строения можно взять из args по индексу.

# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"

# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)

# # Удаление объектов
# del h2
# del h3

# print(House.houses_history)

# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
      if isinstance(other, House):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
      if isinstance(other, House):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
      if isinstance(other, House):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
      if isinstance(other, House):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
      if isinstance(other, House):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
      if isinstance(other, House):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
      if isinstance(value, int):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
      return self.__add__(value)

    def __iadd__(self, value):
      return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
