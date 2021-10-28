import mymodule as my

while True:
    try:
        #my.hello()
        n = int(input('Введите целое число для вычисления \n'
                      'чисел Фибоначчи: '))
        if n > 1:
            print(my.fib(n))
    except Exception:
        print('Неправильное значение')
