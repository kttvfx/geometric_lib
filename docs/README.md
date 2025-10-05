# Math formulas
## General information
Проект представляет набор функций, которые возвращают площади и периметры геометрических фигур по введённым данным 
## Area
- Circle: S = πR²
### Формула возвращает площадь круга 
'''
def area(r):
    return math.pi * r * r
'''
- **example**: if r = 3, then programm output 28.274333882308138

- Rectangle: S = ab
### Формула возвращает площадь прямоугольника
'''
def area(a, b):
    return a * b
'''
- **example**: if a = 4, b = 5, then programm output 20

- Square: S = a²
### Формула фозвращает площадь квадрата
'''
def area(a):
    return a * a
'''
-**example**: if a = 5, then programm output 25

## Perimeter
- Circle: P = 2πR
### Формула возвращает периметр круга 
'''
def perimeter(r):
    return 2 * math.pi * r
'''
-**example**: if r = 2, then programm output 28.274333882308138

### Формула возвращает периметр прямоугольника
- Rectangle: P = 2a + 2b
'''
def perimeter(a, b):
    return 2a + 2b
'''
-**example**: if a = 3, b = 4, than programm output 14

### Формула возвращает периметр квадрата 
- Square: P = 4a    
'''
def perimerter(a):
    return 4*a
'''
-**example**: if a = 3, then programm output 12

# History
**1** commit(8ba9aeb3cea847b63a91ac378a2a6db758682460)
*date* Thu Mar 4 14:54:08 2021
*new* -Circle and square added
**2** commit(d078c8d9ee6155f3cb0e577d28d337b791de28e2)
*date* -Thu Mar 4 14:55:29 2021
*new* -Docs added