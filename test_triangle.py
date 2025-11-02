import unittest
import math
from triangle import area
from triangle import perimeter

class TriangleTestCases(unittest.TestCase):
    '''
    Класс тестов функций area и perimeter из файла triangle.py для рассчета площади и периметра треугольника,
    который содержит тесты для проверки данных функций
    '''
    # Тесты для функции area
    '''Тест площади треугольника с целочисленными положительными сторонами'''
    def test_area_positive_int_triangle_sides(self):
        result = area(3, 4)
        self.assertEqual(result, 0.5 * 3 * 4)
    '''Тест площади треугольника со стороной, равной 0'''
    def test_area_side_is_zero(self):
        with self.assertRaises(ValueError):
            area(0, 3)
    '''Тест площади треугольника с высотой, равной 0'''
    def test_area_height_is_zero(self):
        with self.assertRaises(ValueError):
            area(3, 0)
    '''Тест площади треугольника с дробной положительной стороной и высотой'''
    def test_area_positive_float_triange_side_and_height(self):
        result = area(2.5, 2.5)
        self.assertAlmostEqual(result, 0.5 * 2.5 * 2.5)
    '''Тест площади треугольника с целой большой положительной стороной и высотой'''
    def test_area_positive_big_numbers_triangle_side_and_height(self):
        result = area(999999999, 999999999)
        self.assertEqual(result, 0.5 * 999999999 * 999999999)
    '''Тест площади треугольника с целой малой положительной стороной и высотой'''
    def test_area_positive_little_numbers_triangle_side_and_height(self):
        result = area(0.0001, 0.0001)
        self.assertAlmostEqual(result, 0.5 * 0.0001 * 0.0001)
    '''Тест площади треугольника с целочисленной отрицательной стороной и высотой'''
    def test_area_negative_int_triangle_side_and_height(self):
        with self.assertRaises(ValueError):
            area(-3, -3)
    '''Тест площади треугольника с дробной отрицательной стороной и высотой'''
    def test_area_negative_float_rectangle_side_and_height(self):
        with self.assertRaises(ValueError):
            area(-2.5, -2.5)
    '''Тест площади треугольника со строковыми значениями стороны и высоты'''
    def test_area_input_string_format(self):
        with self.assertRaises(TypeError):
            area("3", "3")
    '''Тест площади треугольника с булевыми типами стороны и высоты'''
    def test_area_input_bool_true_format(self):
        with self.assertRaises(TypeError):
            area(True)
    '''Тест площади прямоугольника со стороной и высотой типа None'''
    def test_area_input_none_format(self):
        with self.assertRaises(TypeError):
            area(None, None)
    '''Тест площади треугольника со списками в качестве ввода данных'''
    def test_area_input_list_format(self):
        with self.assertRaises(TypeError):
            area([12, 24, 36], [23, 45, 56])
    '''Тест для функции area() о выводе сообщения об ошибке для отрицательной стороны и высоты'''
    def test_area_negative_sides_message(self):
        with self.assertRaises(ValueError) as cm:
            area(-4, -8)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест площади треугольника с кортежами в качестве сторон ввода данных'''
    def test_area_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            area((23, 56, 97), (34, 56, 43))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    # Тесты для функции perimeter
    '''Тест периметра треугольника с целочисленными положительными сторонами'''
    def test_perimeter_positive_int_triangle_sides(self):
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 3 + 4 + 5)
    '''Тест периметра треугольника со первой стороной, равной 0'''
    def test_perimeter_first_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
    '''Тест периметра треугольника со второй стороной, равной 0'''
    def test_perimeter_second_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)
    '''Тест периметра треугольника со третьей стороной, равной 0'''
    def test_perimeter_third_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)
    '''Тест периметра треугольника с дробными положительными сторонами'''
    def test_perimeter_positive_float_triange_sides(self):
        result = perimeter(2.5, 2.5, 2.5)
        self.assertAlmostEqual(result, 2.5 + 2.5 + 2.5)
    '''Тест периметра треугольника с целыми большими положительными числами'''
    def test_perimeter_positive_big_numbers_triangle_sides(self):
        result = perimeter(999999999, 999999999, 999999999)
        self.assertEqual(result, 999999999 + 999999999 + 999999999)
    '''Тест периметра треугольника с целыми малыми положительными числами'''
    def test_perimeter_positive_little_numbers_triangle_sides(self):
        result = perimeter(0.0001, 0.0001, 0.0001)
        self.assertAlmostEqual(result, 0.0001 + 0.0001 + 0.0001)
    '''Тест периметра треугольника с целочисленными отрицательными сторонами'''
    def test_perimeter_negative_int_triangle_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, -3, -3)
    '''Тест периметра треугольника с дробными отрицательными сторонами'''
    def test_perimeter_negative_float_triangle_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5, -2.5, -2.5)
    '''Тест периметра треугольника со строковыми значениями сторон'''
    def test_perimeter_input_string_format(self):
        with self.assertRaises(TypeError):
            perimeter("3", "3", "3")
    '''Тест периметра треугольника с булевыми типами сторон'''
    def test_perimeter_input_bool_format(self):
        with self.assertRaises(ValueError):
            perimeter(True, False, False)
    '''Тест периметра треугольника со сторонами типа None'''
    def test_perimeter_input_none_format(self):
        with self.assertRaises(TypeError):
            perimeter(None, None, None)
    '''Тест периметра треугольника со списками в качестве сторон ввода данных'''
    def test_perimeter_input_list_format(self):
        with self.assertRaises(TypeError):
            perimeter([12, 24, 36], [23, 45, 56], [2, 3, 4])
    '''Тест для функции perimeter() о выводе сообщения об ошибке для отрицательных сторон'''
    def test_perimeter_negative_sides_message(self):
        with self.assertRaises(ValueError) as cm:
            perimeter(-4, -8, -52)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест периметра треугольника с кортежами в качестве сторон ввода данных'''
    def test_perimeter_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            perimeter((23, 56, 97), (34, 56, 43), (99, 46, 33))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)

if __name__ == '__main__':
    unittest.main()
