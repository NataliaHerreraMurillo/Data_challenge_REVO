import unittest
import pandas as pd
from dataframe_transformer import DataFrameTransformer

class TestDataFrameTransformer(unittest.TestCase):

    def setUp(self):
        # Sample data setup
        self.sample_data = {
            'userid': [1, 1, 2, 2, 3],
            'km_travelled_in_a_year': [100, 150, 200, 50, 300]
        }
        self.df = pd.DataFrame(self.sample_data)

    def test_group_and_sum(self):
        # Test the group_and_sum method
        transformer = DataFrameTransformer(self.df)
        result_df = transformer.group_and_sum(['userid'], 'km_travelled_in_a_year', 'total_km').get_dataframe()
        
        # Expected result
        expected_data = {
            'userid': [1, 2, 3],
            'total_km': [250, 250, 300]
        }
        expected_df = pd.DataFrame(expected_data)

        # Assert that the result matches the expectation
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()

# To run the tests, you would use the command line to execute the test module.
# Navigate to the directory containing your test_dataframe_transformer.py file and run:
    
# python -m unittest test_dataframe_transformer
