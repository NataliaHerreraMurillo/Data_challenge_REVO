
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def clean_year_column(df, column_name):
    """
    Cleans the year format in a DataFrame column by extracting the first four valuable digits.

    Parameters:
    df (DataFrame): The Pandas DataFrame containing the year column.
    column_name (str): The name of the column to clean.

    Returns:
    DataFrame: The DataFrame with the cleaned year column.
    """
    # Extract the first 4 digits which represent the year
    df[column_name] = df[column_name].str.extract(r'(\d{4})')
    return df



# Function to impute 'Km travelled in a year' using a RandomForestRegressor
def impute_km_with_random_forest(df):
    """
    Imputes missing 'Km travelled in a year' values in a DataFrame using RandomForestRegressor. 
    This function is designed to handle cases where 'hours_travelled_in_a_year' and 'travelmodes' are 
    available, but 'Km travelled in a year' is missing. It achieves this by initially filtering the DataFrame 
    to include only rows with complete data for these key columns. A RandomForestRegressor model is then 
    trained on this filtered dataset. The trained model is subsequently used to predict and impute missing 
    'Km travelled in a year' values in cases where 'hours_travelled_in_a_year' and 'travelmodes' are 
    present. The function employs GridSearchCV for hyperparameter optimization to enhance model 
    performance.

    Parameters:
     df (DataFrame): Pandas DataFrame containing the columns 'km_travelled_in_a_year', 
    'hours_travelled_in_a_year', and 'travelmodes'.

    Returns:
    The original DataFrame with imputed values in the 'km_travelled_in_a_year' column.
    """
    # Filter out rows where 'TravelModes' is missing
    df_filtered = df.dropna(subset=['km_travelled_in_a_year', 'hours_travelled_in_a_year', 'travelmodes'])

    # Split data into training and testing sets
    train_df, test_df = train_test_split(df_filtered, test_size=0.2, random_state=42)

    # Prepare training data
    X_train = train_df[['hours_travelled_in_a_year', 'travelmodes']]
    y_train = train_df['km_travelled_in_a_year']

    # Prepare testing data
    X_test = test_df[['hours_travelled_in_a_year', 'travelmodes']]
    y_test = test_df['km_travelled_in_a_year']

    # Pipeline setup
    pipeline = Pipeline([
        ('preprocessing', ColumnTransformer([
            ('encoder', OneHotEncoder(), ['travelmodes']),
            ('scaler', StandardScaler(), ['hours_travelled_in_a_year'])
        ])),
        ('regressor', RandomForestRegressor(random_state=42))
    ])

    # Hyperparameter grid
    param_grid = {
        'regressor__n_estimators': [200, 500, 1000],
        'regressor__max_depth': [10, 20, None],
        'regressor__min_samples_split': [2, 5, 10],
        'regressor__min_samples_leaf': [1, 2, 4]
    }

    # GridSearchCV setup
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)

    # Fit the model using grid search
    grid_search.fit(X_train, y_train)

    # Best parameters and best model
    best_params = grid_search.best_params_
    print(f"Best Parameters: {best_params}")
    best_model = grid_search.best_estimator_

    # Evaluate the model with the best parameters
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"RMSE with best parameters: {rmse}")

    # Impute missing values in the original DataFrame using the best model
    df_predict = df[df['km_travelled_in_a_year'].isna() & df['hours_travelled_in_a_year'].notna() & df['travelmodes'].notna()]
    X_predict = df_predict[['hours_travelled_in_a_year', 'travelmodes']]
    df_imputed = df
    df_imputed.loc[df_predict.index, 'km_travelled_in_a_year'] = best_model.predict(X_predict)
    return df_imputed
