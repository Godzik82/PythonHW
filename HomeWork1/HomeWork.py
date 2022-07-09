from math import sqrt

def task1():
    print('Задача 1: Создать программу, для решения квадратного уравнения, данные запрашивать у пользователя.')
    sqr = input('Введите через пробел коэффициенты уравнения: ').split()
    sqr = [float(i) for i in sqr]
    d = sqr[1] * sqr[1] - 4 * sqr[0] * sqr[2]
    if d > 0:
        print(f'Корни уравнения равны: {round((-sqr[1] + sqrt(d)) / 2 * sqr[0], 2)} и {round((-sqr[1] - sqrt(d)) / 2 * sqr[0], 2)}\n')
    elif d == 0:
        print(f'Корень уравнения равен: {round(-sqr[1] / 2 * sqr[0], 2)}\n')
    else:
        print('Уравнение не имеет решения\n')

def task2():
    print("""Создать программу, запрашивающую у пользователя два числа и математическую операцию,
             после чего в зависимости от выбранной операции + - / * выполнить указанную операцию""")
    src = input('Введите математическое выражение из двух чисел, используя + - / *: ')
    print(solve(src))

def solve(src):
    if src.find('+') != -1:
        src = split_src(src, '+')
        return src[0] + src[1]
    elif src.find('-') != -1:
        src = split_src(src, '-')
        return src[0] - src[1]
    elif src.find('/') != -1:
        src = split_src(src, '/')
        return src[0] / src[1]
    elif src.find('*') != -1:
        src = split_src(src, '*')
        return src[0] * src[1]
    else:
        return 'Неправильно указана математическая операция'

def split_src(src, operation):
    src = src.split(operation)
    src = [float(i) for i in src if i != operation]
    return src

def main():
    task1()
    task2()

if __name__ == '__main__':
    main()
