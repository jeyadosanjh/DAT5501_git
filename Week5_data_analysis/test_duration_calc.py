import unittest
import pandas as pd
import numpy as np
from duration_calc import difference_in_days

class TestDurationCalc(unittest.TestCase):
    def test_difference_in_days(self):
        # test with a date 10 days in the future
        future_date = (np.datetime64('today', 'D') + np.timedelta64(10, 'D')).astype(str)
        self.assertEqual(difference_in_days(future_date), 10)

        # test with a date 5 days in the past - checking for negative handling
        past_date = (np.datetime64('today', 'D') - np.timedelta64(5, 'D')).astype(str)
        self.assertEqual(difference_in_days(past_date), 5)

        # test with today's date
        today_date = np.datetime64('today', 'D').astype(str)
        self.assertEqual(difference_in_days(today_date), 0)

if __name__ == '__main__':
    unittest.main()
