import mymodule as my

while 1:
    try:
        #my.hello()

        n = int(input('Введите целое число для вычисления \n'
                      'чисел Фибоначчи: '))
        print(my.fib(n))

    except Exception:
        print('Неправильное значение')
