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
```
a1343c244cd4db0297d4cdc6f8718e6c3954328d (HEAD -> main, origin/main, origin/HEAD) add tests for every function, update README.md
6fa27f8e73c1fbd0fc9b8a4c0955985be5981b3e (origin/new_features_467840, new_features_467840) fix documentation
4eaed523e301c6c28e4fbc2863ac6c7ecac5addc add README documentation
21c272a922c676935ffddf12cf5fbfab80edc825 add a comment to each function
855a8ec2d9314558147eabafa70106dd3181c3ad add new file triangle.py, fix rectangle.py
ca0b25dda1362479317b83ce737120364e55b868 add new file rectangle.py
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```

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