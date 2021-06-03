# This file is part production_calendar_color module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class ProductionCalendarColorTestCase(ModuleTestCase):
    'Test Production Calendar Color module'
    module = 'production_calendar_color'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductionCalendarColorTestCase))
    return suite
