from unittest import TestCase

from datetime import datetime
from timewarp.timewarp import Timewarp


class UpdateComponentTest(TestCase):

    def test_init(self):
        expression = ''
        timewarp_obj = Timewarp(expression)

        self.assertTrue(timewarp_obj.is_valid_expression(expression))

    def test_from_timestamp(self):
        init_time = 1234567860
        timewarp_obj = Timewarp(
            '-1m',
            start_datetime=datetime.fromtimestamp(init_time)
        )

        self.assertEqual(
            timewarp_obj.to_datetime().timestamp(),
            init_time - 60
        )

    def test_update_component(self):
        timewarp_obj = Timewarp('', additive=True)

        # Addition:
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 0, 0)
        )

        timewarp_obj.update_component('+1s')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 0, 1)
        )

        timewarp_obj.update_component('+2m')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 2, 1)
        )

        timewarp_obj.update_component('+3h')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 3, 2, 1)
        )

        timewarp_obj.update_component('+4d')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 5, 3, 2, 1)
        )

        timewarp_obj.update_component('+5w')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 2, 9, 3, 2, 1)
        )

        timewarp_obj.update_component('+6mon')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 8, 9, 3, 2, 1)
        )

        timewarp_obj.update_component('+7y')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(8, 8, 9, 3, 2, 1)
        )

        # Subtraction:
        timewarp_obj.update_component('-7y')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 8, 9, 3, 2, 1)
        )

        timewarp_obj.update_component('-6mon')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 2, 9, 3, 2, 1)
        )

        timewarp_obj.update_component('-5w')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 5, 3, 2, 1)
        )

        timewarp_obj.update_component('-4d')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 3, 2, 1)
        )

        timewarp_obj.update_component('-3h')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 2, 1)
        )

        timewarp_obj.update_component('-2m')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 0, 1)
        )

        timewarp_obj.update_component('-1s')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(1, 1, 1, 0, 0, 0)
        )

    def test_update_component_snaps(self):
        timewarp_obj = Timewarp('+2020y+5mon+9d+12h+30m+30s', additive=True)

        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 10, 12, 30, 30)
        )

        timewarp_obj.update_component('@s')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 10, 12, 30, 30)
        )

        timewarp_obj.update_component('@m')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 10, 12, 30, 0)
        )

        timewarp_obj.update_component('@h')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 10, 12, 0, 0)
        )

        timewarp_obj.update_component('@d')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 10, 0, 0, 0)
        )

        timewarp_obj.update_component('@w')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 7, 0, 0, 0)
        )

        timewarp_obj.update_component('@mon')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 6, 1, 0, 0, 0)
        )

        timewarp_obj.update_component('@y')
        self.assertEqual(
            timewarp_obj.to_datetime(), datetime(2021, 1, 1, 0, 0, 0)
        )
