import math
from turtle import color
from math import pi,sqrt
class Figure: #фигура
    sides_count = 0 # кол-во сторон

    def __init__(self,color:tuple,*sides,filled:bool = True):
         self._sides = sides # список сторон инициализируем
         self._color = color # список цветов
         self.filled = filled # флаг, указывает закрашена или нет фигура

        # Проверка на кол-во сторон
         if len(sides) != self.sides_count:
             self._sides = [1]*self.sides_count
         else:
             self._sides = [i for i in sides]

    def get_color(self):
        return self._color # вернет кортеж цветов

    def __len__(self):
        return sum(self._sides)# возвращает периметр фигуры

    def get_sides(self):
        return [*self._sides]# возвращает список сторон

    def __is_valid_color(self,r,g,b):
        # принимает параметры r,g,b проверяет корректность пкркданных значений
        # перед установкой нового цвета - корректность - это целые числа от 0 до 255 включительно
        lst = [r,g,b]
        lst.sort()
        if lst[0]< 0 or lst[-1] > 255:
              return False
        else:
             return True # цвет не корректный


    def set_color(self,r,g,b):
        # принимает параметры r,g,b проверяет на коректность и меняет атрибут color
        # на другой если введены коректные данные, если нет цвет остаётся прежний
        if self.__is_valid_color(r,g,b):
           self._color = (r,g,b)

    def __is_valid_sides(self,sides):
        # принимает неграниченое кол-во сторон возвращает True если все стороны целые
        # положительные числа ,и совподает с текущим кол-вом сторон иначе False
       valid =[]
       for i in sides:
            if i > 0:
                valid.append(i)
                if len(valid) > 0 and len(sides) == len(self._sides):
                    return True
            else:
                    return False

    def set_sides(self,*sides):# принимает новые  стороны  и если их кол-во не равно==0
        # то не изменять, иначе менять
        if self.__is_valid_sides(sides):
           self._sides = sides

class Circle (Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__ * (2/pi)

    # def get_square(self):
    #     x = (self._radius ** 2)* math.pi
    #     return x

class Cube(Figure):
    sides_count = 12

    def __init__(self,color,*sides:int,filled:bool = True):
        super().__init__(color,*sides,filled)
        if len(sides) == 1:
          self._sides = self.sides_count *[i for i in sides]
        else:
          self._sides = [1]*self.sides_count

    def get_sides(self):
        return [*self._sides]
    def get_volume(self):
        return self._sides[1]**3


class Triangle(Figure):
    sides_count = 3

    def __init__(self,color,*sides):
        super().__init__(color,*sides)

    def get_square(self):
        a,b,c = self._sides
        p = (a+b+c)/2
        return math.sqrt(p *(p-a)*(p-b)*(p-c))


circle1 = Circle((200,200,100),10)# цвет стороны
cube1 = Cube((222,35,130),6)

# Проверка на изменение цвета
circle1.set_color(55,66,77)# Измениться
print(circle1.get_color())
cube1.set_color(77,500,15)# Не измениться
print(cube1.get_color())

  #Проверка на изменение сторон
cube1.set_sides(5,3,12,4,5)# Не измениться
print(cube1.get_sides())
circle1.set_sides(15) # Измениться
print(circle1.get_sides())

 # Проверка периметра (круга), это и есть длинна
print(len(circle1))

 # проверка обьёма (куба)
print(cube1.get_volume())

 # площадь
#print(circle1.get_square())





