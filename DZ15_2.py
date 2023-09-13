import argparse
import logging


class Rectangle:
    """
    Класс "Прямоугольник" для выполнения действий с прямоугольниками,
    позволяет сравнивать прямоугольники по площади,
    получить площадь и периметр прямоугольников
    складывать и вычитать прямоугольники
    """

    __slots__ = ('_width', '_length')

    def __init__(self, side_a, side_b=0):
        if side_b == 0:
            side_b = side_a
        try:
            a, b = side_a, side_b
            if side_a <= 0 or side_b <= 0:
                side_b = side_a = 1
                raise ValueError(f"Длина сторон должна быть больше 0. Вы ввели {a} и {b}\n"
                                 f"Стороны будут принят за 1")
        except ValueError as e:
            print(e)
            logger.error(f'Переданные данные: a:"{a}", b"{b}" {e}')
        finally:
            self._width = side_a
            self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        """
        сложение прямоугольников, складываются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после сложения периметров
        """
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """
        вычитание прямоугольников, вычитаются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после вычитания периметров
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        res = f'Прямоугольник со сторонами {self._width} и {self._length}'
        return res




if __name__ == '__main__':
    logging.basicConfig(filename='Log/Rectangle.log',
                        filemode='a',
                        encoding='utf-8',
                        format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-a1', type=str, default='5')
    parser.add_argument('-b1', type=str, default='0')
    parser.add_argument('-a2', type=str, default='10')
    parser.add_argument('-b2', type=str, default='0')
    parser.add_argument('-op', type=str, default='=')

    args = parser.parse_args()

    try:
        a1 = int(args.a1)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона a1 = {args.a1}, {e}')
        a1 = -1
    try:
        b1 = int(args.b1)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона b1 = {args.b1}, {e}')
        b1 = -1

    try:
        a2 = int(args.a2)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона a2 = {args.a2}, {e}')
        a2 = -1

    try:
        b2 = int(args.b2)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона b2 = {args.b2}, {e}')
        b2 = -1


    rectangle1 = Rectangle(a1, b1)
    rectangle2 = Rectangle(a2, b2)
    logger.info(f'получен 1: {(rectangle1)}')
    logger.info(f'получен 2: {(rectangle2)}')


    if args.op == "=":
        print(rectangle1 == rectangle2)
        logger.info(f'Проверка равенства прямоугольника 1 и прямоугольника 2: {(rectangle1 == rectangle2)}')
    elif args.op == ">":
        print(rectangle1 > rectangle2)
        logger.info(f'Проверка что прямоугольник 1 больше прямоугольника 2: {(rectangle1 > rectangle2)}')
    elif args.op == "<":
        print(rectangle1 < rectangle2)
        logger.info(f'Проверка что прямоугольник 1 меньше прямоугольника 2: {(rectangle1 < rectangle2)}')
    elif args.op == "+":
        rectangle3 = rectangle1 + rectangle2
        logger.info(f'При сложении прямоугольника 1 и прямоугольника 2 получен: {rectangle3}')
        print(rectangle3)
    elif args.op == "-":
        rectangle3 = rectangle2 - rectangle1
        logger.info(f'При вычитании прямоугольника 1 из прямоугольника 2 получен: {rectangle3}')
        print(rectangle3)
    else:
        logger.info(f'Передена некорректная операция: {args.op}')
        print(f'Передена некорректная операция: {args.op}')