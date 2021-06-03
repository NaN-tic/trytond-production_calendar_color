# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from datetime import date
from trytond.model import ModelView, fields
from trytond.model import (ModelView, ModelSQL, MatchMixin, fields,
    sequence_ordered)
from trytond.pool import Pool, PoolMeta


class RGB:
    def __init__(self, color=(0, 0, 0)):
        if isinstance(color, str):
            color = color.lstrip('#')
            self.value = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        else:
            self.value = color
        assert isinstance(self.value, tuple)
        assert len(self.value) == 3

    def hex(self):
        return '#%02x%02x%02x' % self.value

    def increase(self, inc):
        res = []
        for x in self.value:
            res.append(max(0, min(255, x + inc)))
        self.value = tuple(res)

    def increase_ratio(self, ratio):
        self.increase(int((255 - self.gray()) * ratio))

    def gray(self):
        return (self.value[0] + self.value[1] + self.value[2]) // 3


class Production(metaclass=PoolMeta):
    __name__ = 'production'

    calendar_color = fields.Function(fields.Char('Color'), 'get_calendar_color')
    calendar_background_color = fields.Function(fields.Char('Background Color'),
        'get_calendar_background_color')

    def get_calendar_color(self, name):
        if self.calendar_background_color:
            rgb = RGB(self.calendar_background_color)
            if rgb.gray() > 128:
                return 'black'
            return 'white'

    def get_calendar_background_color(self, name):
        CalendarColor = Pool().get('production.calendar.color')
        return CalendarColor.compute(self.state)


class ProductionCalendarColor(sequence_ordered(), MatchMixin, ModelSQL,
    ModelView):
    '''Production Calendar Color'''
    __name__ = 'production.calendar.color'

    state = fields.Selection([
            (None, ''),
            ('request', 'Request'),
            ('draft', 'Draft'),
            ('waiting', 'Waiting'),
            ('assigned', 'Assigned'),
            ('running', 'Running'),
            ('done', 'Done'),
            ('cancel', 'Canceled'),
            ], 'State')
    color = fields.Char('Color', help='Add color in hex code (ex. #000000)')

    @classmethod
    def compute(cls, state):
        colors = cls.search([('state', '=', state)], limit=1)
        if colors:
            return colors[0].color
