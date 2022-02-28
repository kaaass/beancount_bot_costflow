import datetime
import os
import unittest

from beancount_bot import transaction
from beancount_bot_costflow import CostflowDispatcher

PATH = os.path.split(os.path.realpath(__file__))[0]


class TestCostflow(unittest.TestCase):

    def test_costflow(self):
        today = datetime.date.today().isoformat()
        cases = [
            ('spotify',
             f'{today} * "Spotify" "" #costflow\n'
             '  Liabilities:CreditCard:Visa  -15.98 USD\n'
             '  Expenses:Subscriptions        15.98 USD\n'),
            ('balance bofa 360',
             f'{today} balance Assets:US:BofA:Checking 360 USD'),
            ('@Verizon bofa -59.61 | phone 59.61',
             f'{today} * "Verizon" "" #costflow\n'
             '  Assets:US:BofA:Checking  -59.61 USD\n'
             '  Expenses:Home:Phone       59.61 USD\n'),
            ('☕️ 4.2',
             f'{today} * "Leplays" "☕️" #costflow\n'
             '  Liabilities:CreditCard:Visa  -4.20 USD\n'
             '  Expenses:Coffee               4.20 USD\n'),
            ('f c2f @KFC 36',
             f'{today} * "KFC" "" #costflow\n'
             '  Liabilities:CreditCard:CMB  -36.00 USD\n'
             '  Expenses:Food                36.00 USD\n'),
            ('@A B 10 bofa > 2 rx + ry',
             f'{today} * "A" "B" #costflow\n'
             '  Assets:US:BofA:Checking  -10.00 USD\n'
             '  Assets:Receivables:X       2.00 USD\n'
             '  Assets:Receivables:Y       8.00 USD\n'),
        ]

        for cmd, expected in cases:
            d = CostflowDispatcher(os.path.join(PATH, 'costflow.json'))
            ret = d.process(cmd)
            actual = transaction.stringfy(ret)
            self.assertEqual(actual, expected)
