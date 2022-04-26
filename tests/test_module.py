
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase


class ProductionCalendarColorTestCase(CompanyTestMixin, ModuleTestCase):
    'Test ProductionCalendarColor module'
    module = 'production_calendar_color'


del ModuleTestCase
