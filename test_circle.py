import unittest
import math
from circle import area
from circle import perimeter

class CircleTestCases(unittest.TestCase):
    '''
    Класс тестов функций area и perimeter из файла circle.py для рассчета площади и периметра круга,
    который содержит тесты для проверки данных функций
    '''
    # Тесты для функции area
    '''Тест площади круга с целочисленным положительным радиусом'''
    def test_area_positive_int_radius(self):
        result = area(3)
        self.assertAlmostEqual(result, math.pi * 3 * 3)
    '''Тест площади круга с радиусом, равным 0'''
    def test_area_is_zero(self):
        result = area(0)
        self.assertEqual(result, math.pi * 0 * 0)
    '''Тест площади круга с дробным положительным радиусом'''
    def test_area_positive_float_radius(self):
        result = area(2.5)
        self.assertAlmostEqual(result, math.pi * 2.5 * 2.5)
    '''Тест площади круга с целыми большими положительными числами'''
    def test_area_positive_big_numbers_radius(self):
        result = area(9999999)
        self.assertEqual(result, math.pi * 9999999 * 9999999)
    '''Тест площади круга с дробными маленькими положительными числами'''
    def test_area_positive_little_numbers_radius(self):
        result = area(0.0001)
        self.assertAlmostEqual(result, math.pi * 0.0001 * 0.0001)
    '''Тест площади круга с целочисленным отрицательным радиусом'''
    def test_area_negative_int_radius(self):
        with self.assertRaises(ValueError):
            area(-3)
    '''Тест площади круга с дробным отрицательным радиусом'''
    def test_area_negative_float_radius(self):
        with self.assertRaises(ValueError):
            area(-2.5)
    '''Тест площади круга со строковым значением радиуса'''
    def test_area_input_string_format(self):
        with self.assertRaises(TypeError):
            area("3")
    '''Тест площади круга с булевым типом радиуса'''
    def test_area_input_bool_true_format(self):
        result = area(True)
        self.assertAlmostEqual(result, math.pi * 1 * 1)
    '''Тест площади круга с булевым типом радиуса'''
    def test_area_input_bool_false_format(self):
        result = area(False)
        self.assertEqual(result, 0)
    '''Тест площади круга с радиусом типа None'''
    def test_area_input_none_format(self):
        with self.assertRaises(TypeError):
            area(None)
    '''Тест площади круга со списком в качестве ввода данных'''
    def test_area_input_list_format(self):
        with self.assertRaises(TypeError):
            area([12, 24, 36])
    '''Тест для функции area() о выводе сообщения об ошибке для отрицательного радиуса'''
    def test_area_negative_radius_message(self):
        with self.assertRaises(ValueError) as cmd:
            area(-4)
        error_message = str(cmd.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест площади круга с кортежем в качестве ввода данных'''
    def test_area_input_tuple(self):
        with self.assertRaises(TypeError) as cmd:
            area((23, 56, 97))
        error_message = str(cmd.exception)
        self.assertIn("Ошибка", error_message)
    # Тесты для функции perimeter
    '''Тест периметра круга с целочисленным положительным радиусом'''
    def test_perimeter_positive_int_radius(self):
        result = perimeter(3)
        self.assertAlmostEqual(result, 2 * math.pi * 3)
    '''Тест периметра круга с радиусом, равным 0'''
    def test_perimeter_is_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 2 * math.pi * 0)
    '''Тест периметра круга с дробным положительным радиусом'''
    def test_perimeter_positive_float_radius(self):
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 2 * math.pi * 2.5)
    '''Тест периметра круга с целыми большими положительными числами'''
    def test_perimeter_positive_big_numbers_radius(self):
        result = perimeter(9999999)
        self.assertEqual(result, 2 * math.pi * 9999999)
    '''Тест периметра круга с целочисленным отрицательным радиусом '''
    def test_perimeter_positive_little_numbers_radius(self):
        result = perimeter(0.0001)
        self.assertAlmostEqual(result, 2 * math.pi * 0.0001)
    '''Тест периметра круга с целочисленным отрицательным радиусом '''
    def test_perimeter_negative_int_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
    '''Тест периметра круга с дробным отрицательным радиусом'''
    def test_perimeter_negative_float_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-2.5)
    '''Тест периметра круга со строковым значением радиуса'''
    def test_perimeter_input_string_format(self):
        with self.assertRaises(TypeError):
            perimeter("3")
    '''Тест периметра круга с булевым типом радиуса'''
    def test_perimeter_input_bool_true_format(self):
        result = perimeter(True)
        self.assertAlmostEqual(result, 2 * math.pi * 1)
    '''Тест периметра круга с булевым типом радиуса'''
    def test_perimeter_input_bool_false_format(self):
        result = perimeter(False)
        self.assertEqual(result, 0)
    '''Тест периметра круга с радиусом типа None'''
    def test_perimeter_input_none_format(self):
        with self.assertRaises(TypeError):
            perimeter(None)
    '''Тест периметра круга со списком в качестве ввода данных'''
    def test_perimeter_input_list(self):
        with self.assertRaises(TypeError):
            perimeter([32, 54, 52])
    '''Тест для функции perimeter() о выводе сообщения об ошибке для отрицательного радиуса'''
    def test_perimeter_negative_radius_message(self):
        with self.assertRaises(ValueError) as cmd:
            perimeter(-4)
        error_message = str(cmd.exception)
        self.assertIn("Ошибка", error_message)
    '''Тест периметра круга с кортежем в качестве ввода данных'''
    def test_perimeter_input_tuple(self):
        with self.assertRaises(TypeError) as cmd:
            perimeter((23, 56, 97))
        error_message = str(cmd.exception)
        self.assertIn("Ошибка", error_message)

if __name__ == '__main__':
    unittest.main()