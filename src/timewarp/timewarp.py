import re

from datetime import (
    datetime,
    timedelta
)


class Timewarp():
    def __init__(self, expression, additive=False, timezone='UTC'):
        '''
        Constructor for a Timewarp object.
        :param expression: The string describing the Timewarp object.
        :kwarg additive: Boolean to specify if we should start from 01/01/0001
                         or not. Default False.
        :kwarg timezone: TODO: Should be pytz timezone object.
        '''
        self.current_time_obj = datetime(1, 1, 1) if additive else datetime.now()
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

        valid_base_regex = '|'.join(valid_base_patterns)

        expression_parts = re.split(r'([+@-])', expression)
        expression_parts = [part for part in expression_parts if part != '']

        parsed_expression = [
            ''.join(expression_parts[i:i + 2]) for i in range(
                0,
                len(expression_parts),
                2
            )
        ]

        for part in parsed_expression:
            if not re.match(valid_base_regex, part):
                return False

        return True

    def update(self, time_expression):
        '''
        Given a Timewarp expression, update self.current_time_obj with that
        expression.
        :param time_expression: A valid Timewarp expression.
        :returns: None
        :raises: Yes. (TODO)
        '''
        if not self.is_valid_expression(time_expression):
            raise InvalidTimewarpExpressionException(
                f'Expression {time_expression} is invalid.'
            )

        pass
