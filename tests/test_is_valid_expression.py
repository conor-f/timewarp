from parameterized import parameterized
from unittest import TestCase

from timewarp.timewarp import Timewarp


class IsValidExpressionTest(TestCase):

    def test_init(self):
        expression = ''
        timewarp_obj = Timewarp(expression)

        self.assertTrue(timewarp_obj.is_valid_expression(expression))

    @parameterized.expand([
        ('simple year snap', '@y'),
        ('simple month snap', '@mon'),
        ('simple week snap', '@w'),
        ('simple day snap', '@d',),
        ('simple hour snap', '@h'),
        ('simple minute snap', '@m'),
        ('simple second snap', '@s'),
        ('simple sub year', '-1y'),
        ('simple sub months', '-10mon'),
        ('simple add weeks', '+234w'),
        ('simple add hours', '+5678h'),
        ('simple sub minutes', '-90001m'),
        ('simple add seconds', '+1234567890s')
    ])
    def test_simple_valid_expressions_are_valid(self, name, expression):
        timewarp_obj = Timewarp('')
        self.assertTrue(timewarp_obj.is_valid_expression(expression))

    def test_wrong_type_is_invalid(self):
        with self.assertRaises(Exception):
            Timewarp(1234)

    @parameterized.expand([
        ('compound year snap month snap', '@y@mon'),
        ('compound day snap hour snap', '@d@h'),
        ('compound week snap hour add', '@w+3h'),
        ('compound second sub minute sub', '-1s-1m'),
        ('compound full composition', '@y-1mon+2w@d-20h+30m@s-200s'),
    ])
    def test_valid_compound_expressions_are_valid(self, name, expression):
        timewarp_obj = Timewarp('')
        self.assertTrue(timewarp_obj.is_valid_expression(expression))

    @parameterized.expand([
        ('bad simple year snap', '@-y'),
        ('bad simple month snap', '-@mon'),
        ('bad simple day snap', '@dd'),
        ('bad simple second add', '++1s'),
        ('bad simple minute sub', '+-1min'),
    ])
    def test_simple_invalid_expressions_are_invalid(self, name, expression):
        timewarp_obj = Timewarp('')
        self.assertFalse(timewarp_obj.is_valid_expression(expression))

    @parameterized.expand([
        ('bad compound year snap month snap', '@ymon+1w'),
        ('bad compound day snap hour snap', '@@dh+1w'),
        ('bad compound day snap invalid char', '@d+1w+2z'),
    ])
    def test_invalid_compound_expressions_are_invalid(self, name, expression):
        timewarp_obj = Timewarp('')
        self.assertFalse(timewarp_obj.is_valid_expression(expression))
