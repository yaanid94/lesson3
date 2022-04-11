# $ - спец. символ для выхода
memory = 0


def my_list():
    return input('Введите набор чисел через пробел:\n').split()


def get_sum(lst, mmr):
    for i in lst:
        if i.isnumeric():
            mmr += int(i)
        elif i == '$':
            print(mmr)
            return False
        else:
            print(f'{i} не является числом')
    print(mmr)
    get_sum(my_list(), mmr)


get_sum(my_list(), memory)
