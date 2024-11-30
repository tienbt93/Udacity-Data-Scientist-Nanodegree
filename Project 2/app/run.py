import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar, Histogram, Layout
import joblib
from sqlalchemy import create_engine
# Import necessary libraries for text processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings
import numpy as np
# Ignore all warnings
warnings.simplefilter('ignore')
# download necessary data from nltk
nltk.download(['punkt_tab', 'stopwords', 'wordnet'])
np.random.seed(42)


app = Flask(__name__)

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

def count_categories_with_value_one(df):
    """
    Count the number of occurrences of the value 1 in each column of the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame to analyze.

    Returns:
        list: A list of tuples, where each tuple contains the column name and the count of values equal to 1 in that column.
    """
    # Drop columns: 'id', 'message', 'original', 'genre'
    columns_to_drop = ['id', 'message', 'original', 'genre']
    df_cleaned = df.drop(columns=columns_to_drop)
    # Create a boolean DataFrame where True indicates the value is 1, then sum the True values per column
    counts = (df_cleaned == 1).sum()
    # Convert the result into a list of tuples: (column name, count of 1s)
    # result = [(column, count) for column, count in counts.items()]
    counts = counts.to_dict()
    print(counts)

    return list(counts.keys()), list(counts.values())

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('disaster_messages', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    category_names, category_counts = count_categories_with_value_one(df)

    df["word_count"] = df["message"].apply(lambda x: len(x.split()))
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Categories',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category"
                }
            }
        },
        # Histogram
        {
        "data": [
            Histogram(
                x=df["word_count"],  # Word count data
                nbinsx=50  # Number of bins in the histogram
            )
        ],
        "layout": Layout(
            title="Messages Word Count Histogram",  # Chart title
            xaxis={"title": "Word Count"},  # X-axis label
            yaxis={"title": "Frequency"},  # Y-axis label
            bargap=0.2  # Gap between bins
        )
    }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()