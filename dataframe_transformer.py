import pandas as pd

import pandas as pd

class DataFrameTransformer:
    """
    A class used to transform a pandas DataFrame with specific operations such as filtering, merging, 
    and grouping of data.

    Attributes
    ----------
    df : DataFrame
        A pandas DataFrame instance that will undergo various transformations.

    Methods
    -------
    filter_by_column_value(column, value):
        Filters the DataFrame based on the value in the specified column.

    merge_multiple_dataframes(merge_operations):
        Merges multiple dataframes with the current dataframe based on the specified operations.

    fill_missing_categorical_values(columns):
        Fills missing values, caused after merging dataframes, in categorical columns with 'Unknown'.

    group_and_sum(group_by_columns, sum_column, sum_column_name):
        Groups the DataFrame by the specified columns and sums up the specified column.

    sort(sort_by, ascending=False):
        Sorts the DataFrame based on the given column(s) in ascending or descending order.

    filter_by_values_in_list(column, values_list):
        Filters the DataFrame to include rows where column values are in the given list.

    count_values(column, count_column_name):
        Counts unique values in a column and creates a new DataFrame with the count.

    reorder_categories(column, categories_to_move):
        Reorders categories in a column, moving specified categories to the end.

    apply_mappings():
        Applies predefined mappings to the 'level_urbanization' and 'mode' columns.

    get_dataframe():
        Returns the transformed DataFrame.
    """

class DataFrameTransformer:
    def __init__(self, df):
        self.df = df

        self.urbanization_level_mapping = {
            'Extremely urbanised': 1,
            'Strongly urbanised': 2,
            'Moderately urbanised': 3,
            'Hardly urbanised': 4,
            'Unknown': 5
        }

        self.travel_method_mapping = {
            'Passenger car (driver)': 1,
            'Passenger car (passenger)': 2,
            'Train': 3,
            'Bus/tram/metro': 4,
            'Bike': 5,
            'Walking': 6,
            'Other': 7,
            'Unknown': 8
        }

    def filter_by_column_value(self, column, value):
        self.df = self.df[self.df[column] == value]
        return self

    def merge_multiple_dataframes(self, merge_operations):
        for df_to_merge, left_on, right_on, how in merge_operations:
            self.df = self.df.merge(df_to_merge, left_on=left_on, right_on=right_on, how=how)
        return self

    def fill_missing_categorical_values(self, columns):
        for column in columns:
            self.df[column].fillna('Unknown', inplace=True)
        return self

    def group_and_sum(self, group_by_columns, sum_column, sum_column_name):
        self.df = self.df.groupby(group_by_columns)[sum_column].sum().reset_index(name=sum_column_name)
        return self
    
    def sort(self, sort_by, ascending=False):
        self.df = self.df.sort_values(by=sort_by, ascending=ascending)
        return self
    
    def filter_by_values_in_list(self, column, values_list):
        self.df = self.df[self.df[column].isin(values_list)]
        return self
    
    def count_values(self, column, count_column_name):
        # Count the frequency of each value in the specified column
        value_counts = self.df[column].value_counts().reset_index()
        value_counts.columns = ['value', count_column_name]
        self.df = value_counts
        return self
    
    def reorder_categories(self, column, categories_to_move):
        self.df = pd.concat([
            self.df[~self.df[column].isin(categories_to_move)],
            self.df[self.df[column].isin(categories_to_move)]
        ], ignore_index=True)
        return self
    
    def apply_mappings(self):
        self.df['urbanization_level_code'] = self.df['level_urbanization'].map(self.urbanization_level_mapping)
        self.df['travel_method_code'] = self.df['mode'].map(self.travel_method_mapping)
        return self

    def get_dataframe(self):
        return self.df
    
    
