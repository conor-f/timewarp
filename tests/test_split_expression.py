from unittest import TestCase

from timewarp.timewarp import Timewarp


class SplitExpressionTest(TestCase):

    def test_init(self):
        expression = ''
        timewarp_obj = Timewarp(expression)

        self.assertTrue(timewarp_obj.is_valid_expression(expression))

    def test_simple_valid_expressions_are_valid(self):
        timewarp_obj = Timewarp('')

        self.assertEqual(
            timewarp_obj.split_expression('@s'), ['@s']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@m'), ['@m']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@h'), ['@h']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@d'), ['@d']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@w'), ['@w']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@mon'), ['@mon']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@y'), ['@y']
        )

        self.assertEqual(
            timewarp_obj.split_expression('+123s'), ['+123s']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123m'), ['+123m']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123h'), ['+123h']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123d'), ['+123d']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123w'), ['+123w']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123mon'), ['+123mon']
        )
        self.assertEqual(
            timewarp_obj.split_expression('+123y'), ['+123y']
        )

        self.assertEqual(
            timewarp_obj.split_expression('-123s'), ['-123s']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123m'), ['-123m']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123h'), ['-123h']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123d'), ['-123d']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123w'), ['-123w']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123mon'), ['-123mon']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-123y'), ['-123y']
        )

        self.assertEqual(
            timewarp_obj.split_expression('@y@mon'), ['@y', '@mon']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@d@h'), ['@d', '@h']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@w+3h'), ['@w', '+3h']
        )
        self.assertEqual(
            timewarp_obj.split_expression('-1s-1m'), ['-1s', '-1m']
        )
        self.assertEqual(
            timewarp_obj.split_expression('@y-1mon+2w@d-20h+30m@s-200s'),
            ['@y', '-1mon', '+2w', '@d', '-20h', '+30m', '@s', '-200s']
        )
