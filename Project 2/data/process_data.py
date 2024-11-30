# import libraries
import sys
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Load and merge datasets for disaster response classification.
    
    This function reads two CSV files, one containing messages and the other containing 
    message categories. It merges the two datasets on the `id` column and returns the 
    resulting dataframe.

    Args:
        messages_filepath (str): Filepath to the CSV file containing messages.
        categories_filepath (str): Filepath to the CSV file containing message categories.

    Returns:
        pd.DataFrame: A dataframe resulting from merging the messages and categories datasets on the `id` column.
    """
    # load messages dataset
    messages = pd.read_csv(messages_filepath)
    # load messages dataset
    categories = pd.read_csv(categories_filepath)
    # merge datasets
    df = messages.merge(categories, how='outer', on=['id'])
    
    return df

def clean_data(df):
    """
    Clean and preprocess the input dataframe for disaster response classification.

    This function splits the `categories` column into individual category columns, 
    converts their values to integers, and combines them with the original dataframe. 
    It also removes duplicates to ensure a clean dataset.

    Args:
        df (pd.DataFrame): The input dataframe containing a `categories` column.

    Returns:
        pd.DataFrame: A cleaned dataframe with individual category columns and duplicates removed.
    """
    # Split the 'categories' column into multiple columns based on the ';' delimiter
    categories = df['categories'].str.split(';', expand=True)

    # Extract the category names (e.g., 'related', 'request', 'offer') by splitting at '-'
    category_colnames = categories.iloc[0].str.split('-', expand=True)[0]
    categories.columns = category_colnames

    # Assign the values (e.g., '1', '0') to the corresponding columns by splitting at '-'
    for column in categories:
        categories[column] = categories[column].str.split('-').str[1].astype(int)

    # Combine the original DataFrame with the new category columns, keeping all other columns
    df = pd.concat([df, categories], axis=1).drop('categories', axis=1)

    # Print the shape of the dataframe and the number of duplicates
    print(df.shape)
    print('number of duplicates:', df.duplicated().sum())

    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df

def save_data(df, database_filename):
    """
    Save the cleaned dataframe to a SQLite database and a CSV file.

    This function saves the provided dataframe to a SQLite database under the table 
    name `disaster_messages` and also exports it to a CSV file.

    Args:
        df (pd.DataFrame): The dataframe to be saved.
        database_filename (str): Filepath for the SQLite database where the data will be saved.

    Returns:
        None
    """
    # Save dataframe to SQLite database
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('disaster_messages', engine, index=False, if_exists='replace')
        
    # Save dataframe to CSV file
    df.to_csv('disaster_messages_merged.csv', index=False)

def main():
    """
    Main function to load, clean, and save disaster response data.

    This function processes disaster response data by:
    1. Loading message and category data from specified filepaths.
    2. Cleaning the combined data to prepare it for machine learning tasks.
    3. Saving the cleaned data into a SQLite database.

    The function expects three command-line arguments:
    1. Filepath to the messages dataset (CSV file).
    2. Filepath to the categories dataset (CSV file).
    3. Filepath for the SQLite database to save the cleaned data.

    If the required arguments are not provided, the function prints usage instructions.

    Command-line Arguments:
        sys.argv[1]: Path to the messages CSV file.
        sys.argv[2]: Path to the categories CSV file.
        sys.argv[3]: Path to the SQLite database file.

    Returns:
        None
    """
    if len(sys.argv) == 4:
        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()