import re

from datetime import datetime
from dateutil.relativedelta import (
    relativedelta,
    MO,
    TU,
    WE,
    TH,
    FR,
    SA,
    SU
)


class Timewarp():
    def __init__(
        self,
        expression,
        start_datetime=None,
        additive=False,
        timezone='UTC'
    ):
        '''
        Constructor for a Timewarp object.
        :param expression: The string describing the Timewarp object.
        :kwarg start_datetime: A datetime object of the point to start from.
        :kwarg additive: Boolean to specify if we should start from 01/01/0001
                         or not. Default False.
        :kwarg timezone: TODO: Should be pytz timezone object.
        '''
        self.current_time_obj = datetime(1, 1, 1) if additive else datetime.now()

        if type(start_datetime) is datetime:
            self.current_time_obj = start_datetime

        self.update(expression)

    def split_expression(self, expression):
        '''
        Given a Timewarp expression, return a list of strings that compose the
        expression.
        :param expression: The string Timewarp expression.
        :returns: list str
        '''
        components = ['']

        for char in expression[::-1]:
            components[-1] = char + components[-1]

            if char in ['@', '+', '-']:
                components.append('')

        return components[:-1][::-1]

    def is_valid_expression(self, expression):
        '''
        Given a Timewarp expression, return True if it is valid, False
        otherwise.
        TODO: Refactor for speedup.
        :param expression: String of the expression
        :returns: Boolean
        '''
        if type(expression) is not str:
            return False

        if expression == '':
            return True

        # Only some chars are allowed in the syntax:
        valid_keywords = ['y', 'mon', 'w', 'd', 'h', 'm', 's']

        valid_base_patterns = [
            r'^@' + valid_keyword + '$' for valid_keyword in valid_keywords
        ]

        valid_base_patterns.extend([
            r'^[+-]\d+' + valid_keyword + '$' for valid_keyword in valid_keywords
        ])

        # Special case for snapping to a specific weekday. e.g. @w4
        valid_base_patterns.extend([r'^@w[\d]$'])

        valid_base_regex = '|'.join(valid_base_patterns)

        for part in self.split_expression(expression):
            if not re.match(valid_base_regex, part):
                return False

        return True

    def update_component(self, c):
        '''
        Given a component of an expression, update the current time object.
        of it.
        '''
        if c[0] == '+' or c[0] == '-':
            if c[-1] == 's':
                self.current_time_obj += relativedelta(seconds=int(c[:-1]))
            elif c[-1] == 'm':
                self.current_time_obj += relativedelta(minutes=int(c[:-1]))
            elif c[-1] == 'h':
                self.current_time_obj += relativedelta(hours=int(c[:-1]))
            elif c[-1] == 'd':
                self.current_time_obj += relativedelta(days=int(c[:-1]))
            elif c[-1] == 'w':
                self.current_time_obj += relativedelta(weeks=int(c[:-1]))
            elif c[-1] == 'n':  # Special case for months.
                self.current_time_obj += relativedelta(months=int(c[:-3]))
            elif c[-1] == 'y':
                self.current_time_obj += relativedelta(years=int(c[:-1]))

        elif c[0] == '@':
            if c[-1] == 's':
                self.current_time_obj = self.current_time_obj.replace(
                    microsecond=0
                )
            elif c[-1] == 'm':
                self.current_time_obj = self.current_time_obj.replace(
                    second=0
                )
                self.update_component('@s')
            elif c[-1] == 'h':
                self.current_time_obj = self.current_time_obj.replace(
                    minute=0
                )
                self.update_component('@m')
            elif c[-1] == 'd':
                self.current_time_obj = self.current_time_obj.replace(
                    hour=0
                )
                self.update_component('@h')
            elif c[-1] == 'w':
                # Special case for weeks:
                self.current_time_obj += relativedelta(weekday=MO(-1))
                self.update_component('@d')
            elif c[-2] == 'w':
                # Special case for weeks:
                if c[-1] == '0':
                    self.current_time_obj += relativedelta(weekday=SU(-1))
                elif c[-1] == '1':
                    self.current_time_obj += relativedelta(weekday=MO(-1))
                elif c[-1] == '2':
                    self.current_time_obj += relativedelta(weekday=TU(-1))
                elif c[-1] == '3':
                    self.current_time_obj += relativedelta(weekday=WE(-1))
                elif c[-1] == '4':
                    self.current_time_obj += relativedelta(weekday=TH(-1))
                elif c[-1] == '5':
                    self.current_time_obj += relativedelta(weekday=FR(-1))
                elif c[-1] == '6':
                    self.current_time_obj += relativedelta(weekday=SA(-1))
                elif c[-1] == '7':
                    self.current_time_obj += relativedelta(weekday=SU(-1))
                self.update_component('@d')
            elif c[-1] == 'n':  # Special condition for months.
                self.current_time_obj = self.current_time_obj.replace(
                    day=1
                )
                self.update_component('@d')
            elif c[-1] == 'y':
                self.current_time_obj = self.current_time_obj.replace(
                    month=1
                )
                self.update_component('@mon')

    def update(self, time_expression):
        '''
        Given a Timewarp expression, update self.current_time_obj with that
        expression.
        :param time_expression: A valid Timewarp expression.
        :returns: None
        :raises: Yes. (TODO)
        '''
        if not self.is_valid_expression(time_expression):
            raise Exception(
                f'Expression {time_expression} is invalid.'
            )

        components = self.split_expression(time_expression)

        for c in components:
            self.update_component(c)

    def to_datetime(self):
        '''
        Returns the datetime representation of this Timewarp object.
        '''
        return self.current_time_obj
