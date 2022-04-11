def my_func(num1, num2, num3):
    tpl = num1, num2, num3
    for i in tpl:
        if i != min(tpl):
            print(i)


my_func(2, 5, 3)
