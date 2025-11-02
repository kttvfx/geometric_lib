import unittest
import math
from square import area
from square import perimeter

class SquareTestCases(unittest.TestCase):
    '''
    Класс тестов функций area и perimeter из файла square.py для рассчета площади и периметра квадрата,
    который содержит тесты для проверки данных функций
    '''
    # Тесты для функции area
    '''Тест площади квадрата с целочисленной положительной стороной'''
    def test_area_positive_int_square_side(self):
        result = area(3)
        self.assertEqual(result, 3 * 3)
    '''Тест площади квадрата со стороной, равной 0'''
    def test_area_side_is_zero(self):
        with self.assertRaises(ValueError):
            area(0)
    '''Тест площади квадрата с дробной положительной стороной'''
    def test_area_positive_float_square_side(self):
        result = area(2.5)
        self.assertAlmostEqual(result, 2.5 * 2.5)
    '''Тест площади квадрата с целым большим положительным числом'''
    def test_area_positive_big_numbers_square_side(self):
        result = area(999999999)
        self.assertEqual(result, 999999999 * 999999999)
    '''Тест площади квадрата с целым малым положительным числом'''
    def test_area_positive_little_numbers_square_side(self):
        result = area(0.0001)
        self.assertAlmostEqual(result, 0.0001 * 0.0001)
    '''Тест площади квадрата с целочисленной отрицательной стороной'''
    def test_area_negative_int_square_side(self):
        with self.assertRaises(ValueError):
            area(-3)
    '''Тест площади квадрата с дробной отрицательной стороной'''
    def test_area_negative_float_square_side(self):
        with self.assertRaises(ValueError):
            area(-2.5)
    '''Тест площади квадрата со строковым значением стороны'''
    def test_area_input_string_format(self):
        with self.assertRaises(TypeError):
            area("3")
    '''Тест площади квадрата с булевым типом стороны'''
    def test_area_input_bool_format(self):
        with self.assertRaises(TypeError):
            area(False)
    '''Тест площади квадрата со стороной типа None'''
    def test_area_input_none_format(self):
        with self.assertRaises(TypeError):
            area(None)
    '''Тест площади квадрата со списком в качестве ввода данных'''
    def test_area_input_list_format(self):
        with self.assertRaises(TypeError):
            area([23, 52, 56])
    '''Тест для функции area() о выводе сообщения об ошибке для отрицательной стороны'''
    def test_area_negative_side_message(self):
        with self.assertRaises(ValueError) as cm:
            area(-30)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест площади квадрата с кортежем в качестве ввода данных'''
    def test_area_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            area((49, 12, 95))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    # Тесты для функции perimeter
    '''Тест периметра квадрата с целочисленной положительной стороной'''
    def test_perimeter_positive_int_square_side(self):
        result = perimeter(3)
        self.assertEqual(result, 4 * 3)
    '''Тест периметра квадрата со стороной, равной 0'''
    def test_perimeter_side_is_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0)
    '''Тест периметра квадрата с дробной положительной стороной'''
    def test_perimeter_positive_float_rectange_side(self):
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 4 * 2.5)
    '''Тест периметра квадрата с целым большим положительным числом'''
    def test_perimeter_positive_big_numbers_square_side(self):
        result = perimeter(999999999)
        self.assertEqual(result, 4 * 999999999)
    '''Тест периметра квадрата с целым малым положительным числом'''
    def test_perimeter_positive_little_numbers_square_side(self):
        result = perimeter(0.0001)
        self.assertAlmostEqual(result, 4 * 0.0001)
    '''Тест периметра квадрата с целочисленной отрицательной стороной'''
    def test_perimeter_negative_int_square_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
    '''Тест периметра квадрата с дробной отрицательной стороной'''
    def test_perimeter_negative_float_square_side(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5)
    '''Тест периметра квадрата со строковым значениям стороны'''
    def test_perimeter_input_string_format(self):
        with self.assertRaises(TypeError):
            perimeter("3")
    '''Тест периметра квадрата с булевым типом стороны'''
    def test_perimeter_input_bool_format(self):
        with self.assertRaises(TypeError):
            perimeter(False)
    '''Тест периметра квадрата со стороной типа None'''
    def test_perimeter_input_none_format(self):
        with self.assertRaises(TypeError):
            perimeter(None)
    '''Тест периметра квадрата со списком в качестве ввода данных'''
    def test_perimeter_input_list_format(self):
        with self.assertRaises(TypeError):
            perimeter([24, 56, 10])
    '''Тест для функции perimeter() о выводе сообщения об ошибке для отрицательной стороны'''
    def test_perimeter_negative_side_message(self):
        with self.assertRaises(ValueError) as cm:
            perimeter(-3)
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест периметра квадрата с кортежем в качестве ввода данных'''
    def test_perimeter_input_tuple(self):
        with self.assertRaises(TypeError) as cm:
            perimeter((10, 20, 30))
        error_message = str(cm.exception)
        self.assertIn("Ошибка", error_message)

if __name__ == '__main__':
    unittest.main()
