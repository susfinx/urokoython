# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом
# подробной информации. Поднимайте исключения внутри основного кода. Например нельзя
# создавать прямоугольник со сторонами отрицательной длины.

# Задание No2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Niga_side_exception (Exception):
    def __init__(self,side: str, side_niga):
        self.side_niga = side_niga
        self.side = side
    def __str__ (self):
        return (f'storona {self.side} ravna {self.side_niga} eto otricatelnoe znachenie, neobhodimo polozhitelnoe chislo')

class Zero_side_exception (Niga_side_exception):
    def __init__(self, side: str, side_niga:int):
        self.side_niga = side_niga
        self.side = side

    def __str__ (self):
        return (f'storona {self.side} = {self.side_niga}, znachenie dolzhno byt bolshe')



class Rectangle:
    def __init__(self,side_a:int, side_b:int = None):
        self.side_a = side_a
        if side_b == None:
            self.side_b=side_a
        else:
            self.side_b = side_b
        if self.side_a < 0:
            raise Niga_side_exception('a', side_a)
        if self.side_b < 0:
            raise Niga_side_exception('b',side_b)
        if self.side_a == 0:
            raise Zero_side_exception('a',0)
        if self.side_b == 0:
            raise Zero_side_exception('b', 0)

    def get_perim (self)->int:
        return 2*self.side_a+2*self.side_b

    def get_square(self)->int:
        return self.side_a*self.side_b

if __name__ =='__main__':
    rect_1=Rectangle(2, 4)
    rect_2=Rectangle(5)
    print(rect_1.get_perim())
    print(rect_1.get_square())
    print(rect_2.get_perim())
    print(rect_2.get_square())
