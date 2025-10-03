import unittest
import pandas as pd
import numpy as np
from synthetic_data import generate_synthetic_data


class TestSyntheticData(unittest.TestCase):
    def test_synthetic_data_generation(self):
        data = generate_synthetic_data()

        # Check if there are no non-numeric values
        self.assertTrue(pd.api.types.is_numeric_dtype(data['x']))
        self.assertTrue(pd.api.types.is_numeric_dtype(data['y']))
        
        # Check if the slope and intercept are close to the defined values
        coeffs = np.polyfit(data['x'], data['y'], 1)
        measured_m, measured_b = coeffs
        self.assertAlmostEqual(measured_m, 4.7, delta=0.5)
        self.assertAlmostEqual(measured_b, 0.3, delta=0.5)

if __name__ == '__main__':
    unittest.main()
