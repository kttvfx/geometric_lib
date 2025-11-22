import math

def area(a, h):
    '''Принимает числа a, h, возвращает площадь треугольника'''

    '''Проверяет тип чисел a, h, возвращает переменную типа str с сообщением об ошибке'''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Ошибка, было введено не число")
    '''Проверяет числа на знак, возвращает переменную типа str с сообщением об ошибке'''
    if (a <= 0) or (h <= 0):
        raise ValueError("Ошибка, было введено не число")  
    return 0.5 * a * h

def perimeter(a, b, c):
    '''Принимает числа a, b, c, возвращает периметр треугольника'''

    '''Проверяет тип чисел a, b, c, возвращает переменную типа str с сообщением об ошибке'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Ошибка, было введено не число")
    '''Проверяет числа на знак, возвращает переменную типа str с сообщением об ошибке'''
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError("Ошибка, было введено не число")  
    return a + b + c

name: CI/CD LAB №5 Python UnitTests 
on: [push]
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13.5'
    - name: Run Python UnitTests
      run: 
        python3 -m unittest

