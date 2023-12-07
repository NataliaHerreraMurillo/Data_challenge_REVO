# Revo Data Challenge

## Description
This repository contains the code and analysis for the "Revo Data Challenge". The challenge involves creating a database to store trip data, conducting exploratory data analysis, and answering specific questions with visualizations in PowerBI.

The project is structured into a Jupyter Notebook that handles the data retrieval, cleaning, and exploratory analysis, and a set of Python modules that contain refactored production-ready code.

## Installation

To set up your environment to run this code, you will need Python and the following packages:
- psycopg2 or equivalent for database interaction
- pandas for data manipulation
- sklearn for data imputation

Additionally, you will need to have PostgreSQL or another relational database running with the provided data.

## Documentation and Tests

Each Python module within this codebase is thoroughly documented with comments explaining the functionality of the classes and methods. This documentation provides insights into the design and usage of the code, making it easier for new contributors to understand and work with the project.

Unit tests have been written to ensure the reliability and correctness of the code. These tests can be found in files within the project that are prefixed with `test_` followed by the name of the module they are testing (e.g., `test_database_handler.py`). To run the tests, navigate to the project's root directory and execute:

```bash
python -m unittest discover -s tests

