
# Sparkify Project

Welcome to the Sparkify Project! This repository demonstrates a data analysis and machine learning pipeline using PySpark to explore and predict user behavior for a music streaming service. The project uses a subset of the dataset to analyze user interactions, detect patterns, and build models for user churn prediction.


---

## Project Overview

The Sparkify Project is designed to:
1. Analyze user data to identify behavioral trends.
2. Explore and clean the dataset to prepare it for machine learning.
3. Define the churn label based on user activities.
4. Train models to predict user churn using PySpark MLlib.

Details of the project can be found in the notebook and blog post on [Sparkify Project](Sparkify-Blog.md)

---

## Dataset `mini_sparkify_event_data.json`

The dataset consists of user interactions, such as:
- Listening history
- User demographics
- Session details
- Activity types (e.g., song playback, account cancellation)

The provided workspace contains a smaller subset (128MB) for local exploration before deploying a full Spark cluster on the cloud.

---

## Tools and Libraries

This project uses the following tools and libraries:
- **PySpark**: For distributed data processing and machine learning.
- **Matplotlib & Seaborn**: For data visualization.
- **Pandas & Numpy**: For auxiliary data manipulations.

---

## Exploratory Data Analysis (EDA)

Key steps during EDA:
1. **Define Churn**: Mark users with "Cancellation Confirmation" events as churned.
2. **Data Cleaning**: Remove null or invalid entries for key columns like `userId` and `sessionId`.
3. **Feature Exploration**: Analyze user demographics, membership duration, and engagement metrics.
4. **Visualization**: Plot distributions of key features like user actions, listening time, and churn.

---

## Model Building

Steps for model building:
1. Feature engineering, including user activity patterns and demographics.
2. Training machine learning models using PySpark’s MLlib library.
3. Evaluation of models using metrics like precision, recall, and F1 score.

---

## Results

Visualizations and insights from the EDA include:
- Churn distribution
- Impact of listening time, gender, and membership level on churn
- User activity trends

Models predict churn based on engineered features, enabling Sparkify to retain at-risk users.

---

## How to Use

1. **Setup**: Install dependencies using `pip install -r requirements.txt`.
2. **Run Analysis**: Execute the [Jupyter Notebook](Sparkify-EDA.ipynb) for EDA and [model training](Sparkify-AI-Model.ipynb).
3. **Deploy Models**: Use the trained model in a production Spark cluster for real-time churn prediction.

---

## Future Work

1. Extend analysis to the full dataset (12GB) using a cloud-based Spark cluster.
2. Experiment with additional features and advanced machine learning algorithms.
3. Integrate predictions into Sparkify's user retention strategy.

--- 

Feel free to explore, extend, and deploy the project for your own applications!
