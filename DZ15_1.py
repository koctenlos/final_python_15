"""
Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.
"""
import argparse
import logging
from math import sqrt


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (f'Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
    elif d == 0:
        x1 = -b / (2 * a)
        return (f'Корень уравнения: x = {x1:.3f}')
    else:
        real = round(-b / (2 * a), 4)
        imaginary = round(sqrt(abs(d)) / (2 * a), 4)
        x1 = complex(real, imaginary)
        x2 = complex(real, -imaginary)
        return (f'Корни уравнения: x1 = {x1}; x2 = {x2}')


if __name__ == '__main__':
    logging.basicConfig(filename='Log/quadratic.log',
                        filemode='a',
                        encoding='utf-8',
                        format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-a', type=str, default='-5')
    parser.add_argument('-b', type=str, default='5')
    parser.add_argument('-c', type=str, default='0')

    args = parser.parse_args()

    try:
        a = int(args.a)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент a:"{args.a}", {e}')

    try:
        b = int(args.b)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент b:"{args.b}", {e}')

    try:
        c = int(args.c)
    except ValueError as e:
        logger.error(f'Переданные данные: коэффициент a:"{args.c}", {e}')

    try:
        res = quadratic_equation(a, b, c)
        logger.info(f'Решение уравнения: {a}x^2 + ({b})x + ({c}) = 0 , {res}')
        print(res)
    except NameError as e:
        logger.error(f'Переданные данные: коэффициенты a:={args.a}, b={args.b}, c={args.c}", ошибка: {e}')
        print('Переданы некорректные данные, см: Log/quadratic.log')


    #>> (решение по умолчанию без пердачи корней)
    #>> (-a="five" -b=5 -c=1)
    #>> (-a=-18 -b=60 -c=100)
    # 'Корни уравнения: x1 = -1.220; x2 = 4.553'
    #>> (-a=5 -b=-10 -c=5)
    # 'Корень уравнения: x = 1.000'
    #>> (-a=5 -b=10 -c=15)
    # 'Корни уравнения: x1 = (-1+1.4142j); x2 = (-1-1.4142j)'