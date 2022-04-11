a = input('Enter the first number: ')
b = input('Enter the second number: ')


def divided(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return 'Нельзя делить на ноль'
    except ValueError:
        return 'Введите число'


print(divided(a, b))
