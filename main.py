import mymodule as my

while True:
     try:
        #my.hello()
        n = int(input('Введите целое число для вычисления \n'
                      'чисел Фибоначчи: '))
        if n <= 0:
            print('Неправильное значение!Введите число больше 0. ')
        elif n > 1:
            print(my.fib(n))
     except Exception:
         print('Неправильное значение. Введите числовой формат.')
