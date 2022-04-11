def my_func(x, y):
    multiplier = x
    while y < -1:
        y += 1
        x *= multiplier
    return 1 / x


print(my_func(2.12, -3))
