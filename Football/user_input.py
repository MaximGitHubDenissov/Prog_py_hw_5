
def team_input(n):
    tm_name = input(f'Введите название {n} команды: ')
    return tm_name

def score_input(n):
    scr = int(input(f'Сколько голов забила команда {n}?: '))
    return scr

def date_input():
    date = input('Дата встречи: ')
    return date

def main_menu():
    print('====Меню турнирной таблицы====\n\
        1 - Записать результаты встречи\n\
        2 - Посмотреть турнирную таблицу\n\
        3 - Посмотреть результаты встреч')
    while True:
        set = input(': ')
        if set in ['1','2','3']:
            return set
        else: print('Недопустимый ввод!')

