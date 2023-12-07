import pandas as pd

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
    
    
