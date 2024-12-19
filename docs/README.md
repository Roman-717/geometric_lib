# Описание библиотеки
Библиотека содержит в себе функции для вычисления площади и периметра таких фигур, как: круг, прямоугольник, квадрат, треугольник.

# Описание функций 

## Circle.py
- def area(r) - Принимает число r - радиус окружности, возвращает площадь круга с радиусом r
- def perimeter(r) - Принимает число r - радиус окружности, возвращает периметр окружности с радиусом r

## Rectangle.py
- def area(a, b) - Принимает два числа a и b - длины сторон прямоугольника, возвращает площадь этого прямоугольника
- def perimeter(a, b) - Принимает два числа a и b - длины сторон прямоугольника, возвращает периметр этого прямоугольника

## Square.py
- def area(a) - Принимает число a - длину стороны квадрата, возвращает площадь этого квадрата
- def perimeter(a) - Принимает число a - длину стороны квадрата, возвращает периметр этого квадрата

## Triangle.py
- def area(a, h) - Принимает два числа: a - длину стороны треугольника и h - длину высоты, проведенной к стороне a, возвращает площадь этого треугольника
- def perimeter(a, b, c) - Принимает три числа a, b и c - длины сторон треугольника, возвращает периметр этого треугольника

# Тесты

Папка tests содержит в себе тесты для каждой функции каждого файла библиотеки.
Каждый test_ файл импортирует пакет unittest и те функции, которые он тестирует.
Пример теста функции area для circle.py: 

```python
import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    ...

    def test_area_second(self):
        self.assertAlmostEqual(area(15), 706.8583, places=4)
        
    ...
```

# Граф изменения проекта 
\* b6f3ec505312ee247fb68be05ea79aa998c5e717 (HEAD -> new_features_467840) Add a comment for each function\
\* 274af56a57df1ff5fa92af78ef36ce469cc2b5ed add new file triangle.py, fix rectangle.py\
\* a820fc14517af6463b03dd887f0d6b4c88b40d0e add new file rectangle.py\
| * 86edb1c3dd57fa9abc7ba2ec7052507938084727 (origin/release) L-05: Update Docs. Add user agreement info\
| * 438b89a1dfc58d90e9036fe431771427965cd1ff L-05: Add user agreement\
| * 6adb96248a4d00d3bea13bd95d78ef52352cd1b4 L-03: Docs added\
| | * 30494317cde4419be779c14306561e0eaa78b88b (origin/feature) L-04: Add rectangle.py\
| |/  \
|/|   \
| | * b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop) L-04: Update docs for calculate.py\
| | * d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py\
| | * 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle\
| | * d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added\
| |/  \
|/|   \
\* | d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added\
|/  \
:

# Формулы

## Площадь
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

## Периметр
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c