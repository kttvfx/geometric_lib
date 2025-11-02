import unittest
import math
from rectangle import area
from rectangle import perimeter

class RectangleTestCases(unittest.TestCase):
    '''
    Класс тестов функций area и perimeter из файла rectangle.py для рассчета площади и периметра прямоугольника,
    который содержит тесты для проверки данных функций
    '''
    # Тесты для функции area
    '''Тест площади прямоугольника с целочисленными положительными сторонами'''
    def test_area_positive_int_rectangle_sides(self):
        result = area(3, 4)
        self.assertEqual(result, 3 * 4)
    '''Тест площади прямоугольника со стороной, равной 0'''
    def test_area_first_side_is_zero(self):
        with self.assertRaises(ValueError):
            area(0, 3)
    '''Тест площади прямоугольника со стороной, равной 0'''
    def test_area_second_side_is_zero(self):
        with self.assertRaises(ValueError):
            area(3, 0)
    '''Тест площади прямоугольника с дробными положительными сторонами'''
    def test_area_positive_float_rectange_sides(self):
        result = area(2.5, 2.5)
        self.assertAlmostEqual(result, 2.5 * 2.5)
    '''Тест площади прямоугольника с целыми большими положительными числами'''
    def test_area_positive_big_numbers_rectangle_sides(self):
        result = area(999999999, 999999999)
        self.assertEqual(result, 999999999 * 999999999)
    '''Тест площади прямоугольника с целыми малыми положительными числами'''
    def test_area_positive_little_numbers_rectangle_sides(self):
        result = area(0.0001, 0.0001)
        self.assertAlmostEqual(result, 0.0001 * 0.0001)
    '''Тест площади прямоугольника с целочисленными отрицательными сторонами'''
    def test_area_negative_int_rectangle_sides(self):
        with self.assertRaises(ValueError):
            area(-3, -3)
    '''Тест площади прямоугольника с дробными отрицательными сторонами'''
    def test_area_negative_float_rectangle_sides(self):
        with self.assertRaises(ValueError):
            area(-2.5, -2.5)
    '''Тест площади прямоугольника со строковыми значениями сторон'''
    def test_area_input_string_format(self):
        with self.assertRaises(TypeError):
            area("3", "3")
    '''Тест площади прямоугольника с булевыми типами сторон'''
    def test_area_input_bool_format(self):
        with self.assertRaises(ValueError):
            perimeter(True, False)
    '''Тест площади прямоугольника со сторонами типа None'''
    def test_area_input_none_format(self):
        with self.assertRaises(TypeError):
            area(None, None)
    '''Тест площади прямоугольника со списками в качестве сторон ввода данных'''
    def test_area_input_list_format(self):
        with self.assertRaises(TypeError):
            area([12, 24, 36], [23, 45, 56])
    '''Тест для функции area() о выводе сообщения об ошибке для отрицательных сторон'''
    def test_area_negative_sides_message(self):
        with self.assertRaises(ValueError) as cm:
            area(-4, -8)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест площади прямоугольника с кортежами в качестве сторон ввода данных'''
    def test_area_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            area((23, 56, 97), (34, 56, 43))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    # Тесты для функции perimeter
    '''Тест периметра прямоугольника с целочисленными положительными сторонами'''
    def test_perimeter_positive_int_rectangle_sides(self):
        result = perimeter(3, 4)
        self.assertEqual(result, 2 * 3 + 2 * 4)
    '''Тест периметра прямоугольника со стороной, равной 0'''
    def test_perimeter_first_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0, 3)
    '''Тест периметра прямоугольника со стороной, равной 0'''
    def test_perimeter_second_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(3, 0)
    '''Тест периметра прямоугольника с дробными положительными сторонами'''
    def test_perimeter_positive_float_rectange_sides(self):
        result = perimeter(2.5, 2.5)
        self.assertAlmostEqual(result, 2 * 2.5 + 2 * 2.5)
    '''Тест периметра прямоугольника с целыми большими положительными числами'''
    def test_perimeter_positive_big_numbers_rectangle_sides(self):
        result = perimeter(999999999, 999999999)
        self.assertEqual(result, 2 * 999999999 + 2 * 999999999)
    '''Тест периметра прямоугольника с целыми малыми положительными числами'''
    def test_perimeter_positive_little_numbers_rectangle_sides(self):
        result = perimeter(0.0001, 0.0001)
        self.assertAlmostEqual(result, 2 * 0.0001 + 2 * 0.0001)
    '''Тест периметра прямоугольника с целочисленными отрицательными сторонами'''
    def test_perimeter_negative_int_rectangle_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, -3)
    '''Тест периметра прямоугольника с дробными отрицательными сторонами'''
    def test_perimeter_negative_float_rectangle_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5, -2.5)
    '''Тест периметра прямоугольника со строковыми значениями сторон'''
    def test_perimeter_input_string_format(self):
        with self.assertRaises(TypeError):
            perimeter("3", "3")
    '''Тест периметра прямоугольника с булевыми типами сторон'''
    def test_perimeter_input_bool_format(self):
        with self.assertRaises(ValueError):
            perimeter(True, False)
    '''Тест периметра прямоугольника со сторонами типа None'''
    def test_perimeter_input_none_format(self):
        with self.assertRaises(TypeError):
            perimeter(None, None)
    '''Тест периметра прямоугольника со списками в качестве сторон ввода данных'''
    def test_perimeter_input_list_format(self):
        with self.assertRaises(TypeError):
            perimeter([12, 24, 36], [23, 45, 56])
    '''Тест для функции perimeter() о выводе сообщения об ошибке для отрицательных сторон'''
    def test_perimeter_negative_sides_message(self):
        with self.assertRaises(ValueError) as cm:
            perimeter(-4, -8)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест периметра прямоугольника с кортежами в качестве сторон ввода данных'''
    def test_perimeter_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            perimeter((23, 56, 97), (34, 56, 43))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)

if __name__ == '__main__':
    unittest.main()
