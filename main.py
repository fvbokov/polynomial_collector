import copy
from matrix import SquareMatrix
from polynomial import Polynomial, Monomial
from read import read_polynomial

user_input = input("Пожалуйста, введите многочлен в формате \'1 + 3x^2 - x + 8\'\nОбязательно ставьте пробелы между знаками и одночленами.\nЕсли для проверки работы программы вас устраивает многочлен выше, введите \'skip\'.\n")
if "skip" in user_input:
    user_input = "1 + 3x^2 - x + 8"

while True:
    print("Выбор операций:")
    print("1. Прибавление константы")
    print("2. Сложение многочленов")
    print("3. Демонстрация нулевого многочлена")
    print("4. Вычитание константы")
    print("5. Вычитание многочленов")
    print("6. Отрицание многочлена")
    print("7. Умножение на константу")
    print("8. Умножение на другой многочлен")
    print("9. Возведение многочлена в натуральную степень")
    print("10. Подстановка вида x + k")
    print("11. Подстановка вида kx")
    print("12. Вычисление многочлена в заданной точке")
    print("13. Вычисление многочлена при подстановке квадратной матрицы")
    print("0. Выход")
    command = int(input())

    polynom = read_polynomial(user_input)

    if command == 1:
        n = int(input("Введите целое число: "))
        print(Polynomial.const_polynomial(n))
        print('+')
        print(polynom)
        print('=') 
        print(Polynomial.add_const(polynom, n), "\n")

        input('Введите Enter для продолжения...')
    elif command == 2:
        second_polynom = input("Введите еще 1 многочлен или \'skip\' для сложения с заготвленным многочленом:\n")
        if "skip" in second_polynom:
            second_polynom = read_polynomial("x + 2 - 5x^3 + 2x^2")
            print('here')
        else:
            second_polynom = read_polynomial(second_polynom)
        print(polynom)
        print('+')
        print(second_polynom)
        print('=') 
        print(Polynomial.add(polynom, second_polynom), "\n")

        input('Введите Enter для продолжения...')
    elif command == 3:
        print('Это нулевой многочлен')
        print(Polynomial.zero_polynomial())
        input('Введите Enter для продолжения...')

    elif command == 4:
        n = int(input("Введите целое число: "))
        print(polynom)
        print('-')
        print(Polynomial.const_polynomial(n))
        print('=') 
        print(Polynomial.substract_const(polynom, n), "\n")

        input('Введите Enter для продолжения...')
    elif command == 5:
        second_polynom = input("Введите еще 1 многочлен или \'skip\' для вычитания с заготвленным многочленом:\n")
        if "skip" in second_polynom:
            second_polynom = read_polynomial("x + 2 - 5x^3 + 2x^2")
        else:
            second_polynom = read_polynomial(second_polynom)
        print(polynom)
        print('-')
        print(second_polynom)
        print('=') 
        print(Polynomial.substract(polynom, second_polynom), "\n")
        input('Введите Enter для продолжения...')

    elif command == 6:
        print("Отрицание многочлена")
        print(polynom)
        print(Polynomial.opposite_polynomial(polynom), "\n")
        input('Введите Enter для продолжения...')

    elif command == 7:
        n = int(input("Введите целое число: "))
        print(polynom)
        print('*')
        print(Polynomial.const_polynomial(n))
        print('=') 
        print(Polynomial.multiply_by_const(polynom, n), "\n")

        input('Введите Enter для продолжения...')

    elif command == 8:
        second_polynom = input("Введите еще 1 многочлен или \'skip\' для умножения с заготвленным многочленом:\n")
        if "skip" in second_polynom:
            second_polynom = read_polynomial("x + 2 - 5x^3 + 2x^2")
        else:
            second_polynom = read_polynomial(second_polynom)
        print(polynom)
        print('*')
        print(second_polynom)
        print('=') 
        print(Polynomial.multiply(polynom, second_polynom), "\n")

        input('Введите Enter для продолжения...')

    elif command == 9:
        n = int(input("Введите целое число: "))
        print(Polynomial.raise_to_a_power(polynom, n), "\n")

        input('Введите Enter для продолжения...')

    elif command == 10:
        n = int(input("Введите целое число: "))
        print(f"x -> x +({n})")
        print(polynom)
        print(Polynomial.transform_horizontally(polynom, n), "\n")

        input('Введите Enter для продолжения...')


    elif command == 11:
        n = int(input("Введите целое число: "))
        print(f"x -> {n}x")
        print(polynom)
        print(Polynomial.transform_vertically(polynom, n), "\n")
        input('Введите Enter для продолжения...')
    
    elif command == 12:
        n = int(input("Введите целое число: "))
        print(f"f({n})")
        print(polynom)
        print(polynom.value(n), "\n")
        input('Введите Enter для продолжения...')

    elif command == 13:
        print("Подстановка квадратной матрицы [[1, 2], [3, 4]]\n")
        A = SquareMatrix(2, [[1, 2], [3, 4]])
        print(polynom.matrix_value(A), "\n")
        input('Введите Enter для продолжения...')

    elif command == 0:
        break

