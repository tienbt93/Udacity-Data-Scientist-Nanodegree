import sys
import warnings
import pandas as pd
import numpy as np
import pickle
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
# Import necessary libraries for text processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ignore all warnings
warnings.simplefilter('ignore')
# download necessary data from nltk
nltk.download(['punkt_tab', 'stopwords', 'wordnet'])
np.random.seed(42)

def load_data(database_filepath):
    """
    Load data from SQLite database and prepare features and target variables.

    Args:
        database_filepath (str): Filepath to the SQLite database.

    Returns:
        X (pd.Series): Message data (features).
        Y (pd.DataFrame): Categories data (target variables).
        category_names (list): List of category names.
    """
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table('disaster_messages', engine)
    X = df['message']
    Y = df.iloc[:, 4:]  # Assuming the first four columns are not target variables
    category_names = Y.columns.tolist()
    return X, Y, category_names

def tokenize(text):
    """
    Tokenize and process text data.

    Args:
        text (str): Input text to tokenize.

    Returns:
        list: List of processed tokens.
    """
    

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    clean_tokens = [lemmatizer.lemmatize(token).lower().strip() 
                    for token in tokens if token.lower() not in stop_words]
    return clean_tokens

def build_model():
    """
    Build a machine learning pipeline with GridSearchCV for hyperparameter tuning.

    Returns:
        GridSearchCV: GridSearchCV object with pipeline and parameter grid.
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize, token_pattern=None)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier(n_jobs=-1)))
    ])
    
    parameters = {
        'clf__estimator__n_estimators': [10, 50, 100],
        'clf__estimator__min_samples_split': [2, 4],
    }
    
    model = GridSearchCV(pipeline, param_grid=parameters, cv=3, verbose=3)
    return model

def evaluate_model(model, X_test, Y_test, category_names):
    """
    Evaluate the model's performance on test data.

    Args:
        model: Trained model.
        X_test (pd.Series): Test features.
        Y_test (pd.DataFrame): Test target variables.
        category_names (list): List of category names.

    Returns:
        None
    """
    Y_pred = model.predict(X_test)
    for i, column in enumerate(category_names):
        print(f"Category: {column}")
        print(classification_report(Y_test.iloc[:, i], Y_pred[:, i]))

def save_model(model, model_filepath):
    """
    Save the trained model to a file.

    Args:
        model: Trained model.
        model_filepath (str): Filepath to save the model.

    Returns:
        None
    """
    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)

def main():
    """
    Main function to load data, build model, train model, evaluate model, and save it.

    Returns:
        None
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')

if __name__ == '__main__':
    main()