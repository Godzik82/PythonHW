def solve(xy):
    try:
        xy = [int(i) for i in xy]
        return 'Частное равно '  + str(xy[0] / xy[1])
    except Exception as a:
        return 'Ошибка - ' + str(a)

def menu():
    xy = input('Введите через пробел два числа: ').split()
    print(solve(xy))
        
def task1():
    choose = 'Y'
    while  choose == 'Y':
        menu()
        choose = input('Будете вводить ещё числа (Y/N)? ')
