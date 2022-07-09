def check_move(start_cordinats, end_cordinats):
    x = abs(ord(start_cordinats[0]) - ord(end_cordinats[0]))
    y = abs(int(start_cordinats[1]) - int(end_cordinats[1]))
    if x + y == 3:
        return True
    else:
        return False

def check_cordinat(start_cordinats, end_cordinats):
    if 'ABCDEFGH'.find(start_cordinats[0]) == -1 or '12345678'.find(start_cordinats[1]) == -1:
        return False
    if 'ABCDEFGH'.find(end_cordinats[0]) == -1 or '12345678'.find(end_cordinats[1]) == -1:
        return False
    return check_move(start_cordinats, end_cordinats)
    

def executor():
    start_cordinats = input('Введите начальные координаты фигуры (например, "D3"): \n')
    end_cordinats = input('Введите конечные координаты фигуры (например, "F2"): \n')
    print('Ответ: ' + str(check_cordinat(start_cordinats, end_cordinats)))

def menu():
    choose = 1
    while choose == 1:
        try:
            choose = int(input('\n___МЕНЮ___\n1) ввести данные\n2) выход\n'))
            if choose == 1:
                executor()
        except ValueError as ex:
            print(f'Ошибка ввода: {ex}')
            # choose == 1
    return 'До свидание!!!'

def main():
    print(menu())

if __name__ == "__main__":
    main()