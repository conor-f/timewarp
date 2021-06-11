from datetime import (
    datetime,
    timedelta
)


class Timewarp():
    def __init__(expression, additive=False, timezone='UTC'):
        '''
        Constructor for a Timewarp object.
        :param expression: The string describing the Timewarp object.
        :kwarg additive: Boolean to specify if we should start from 01/01/0001
                         or not. Default False.
        :kwarg timezone: TODO: Should by pytz timezone object.
        '''
        self.current_time_obj = datetime(1, 1, 1) if additive else datetime.now()
        self.update(expression)

    def is_valid_expression(self, expression):
        '''
        Given a Timewarp expression, return True if it is valid, False
        otherwise.
        :param expression: String of the expression
        :returns: Boolean
        '''
        if not type(expression) is str:
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
