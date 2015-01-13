from datetime import datetime

from django.forms import ValidationError


class Filter(object):
    '''
    Provides casting and validation functions for Fields.
    '''
    @staticmethod
    def to_python(value):
        return value

    @staticmethod
    def from_python(value):
        return value


class NotNullFilter(Filter):
    @staticmethod
    def to_python(value):
        if value is None:
            raise ValidationError('May not be null')
        return value


class _CastFilter(Filter):
    @classmethod
    def to_python(self, value):
        if value is None:
            return value
        return self.type_class(value)


class BooleanFilter(_CastFilter):
    @staticmethod
    def to_python(value):
        if value is None:
            return value
        return value.lower() in (1, '1', 't', 'y', 'true', True)


class IntegerFilter(_CastFilter):
    type_class = int


class FloatFilter(_CastFilter):
    type_class = float


class TimeFilter(object):
    @staticmethod
    def to_python(value):
        return datetime.strptime(value, '%H:%M:%S').time()

    @staticmethod
    def from_python(value):
        if value is None:
            return value
        return value.isoformat()


class DateFilter(object):
    @staticmethod
    def to_python(value):
        return datetime.strptime(value, '%Y-%m-%d').date()

    @staticmethod
    def from_python(value):
        if value is None:
            return value
        return value.isoformat()


class DateTimeFilter(object):
    @staticmethod
    def to_python(value):
        return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def from_python(value):
        if value is None:
            return value
        return value.isoformat(' ')
