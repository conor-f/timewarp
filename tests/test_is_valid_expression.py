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

    @parameterized.expand([
        ('compound year snap month snap', '@y@mon'),
        ('compound day snap hour snap', '@d@h'),
        ('compound week snap hour add', '@w+3h'),
        ('compound second sub minute sub', '-1s-1min'),
        ('compound full composition', '@y-1mon+2w@d-20h+30min@s-200s'),
    ])
    def test_compound_expressions_are_valid(self, name, expression):
        timewarp_obj = Timewarp('')
        self.assertTrue(timewarp_obj.is_valid_expression(expression))
