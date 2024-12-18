# Leveraging AI to Understand and Predict User Behavior: Sparkify Case Study

The Sparkify project showcases how exploratory data analysis (EDA), feature engineering, and machine learning come together to solve a real-world challenge: understanding user behavior to predict customer churn. Here’s an in-depth walkthrough of the process, supported by visualizations and analysis.

![](images\thumbnail.webp)
---

## Table of Contents

1. [Dataset Overview](#dataset-overview)
2. [Data Cleaning](#data-cleaning)
   - [Resulting Dataset](#resulting-dataset)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Defining Churn](#defining-churn)
   - [Behavioral Insights](#behavioral-insights)
4. [Feature Engineering](#feature-engineering)
5. [Model Training](#model-training)
   - [Model Selection](#model-selection)
   - [Training Process](#training-process)
   - [Random Forest Tuning](#random-forest-tuning)
6. [Results](#results)
   - [Model Performance](#model-performance)
   - [Key Insights](#key-insights)
7. [Conclusion](#conclusion)

---

## Dataset Overview

Sparkify provides user interaction logs, allowing us to analyze behaviors and predict churn (user cancellation). For this project, we used a subset of the dataset, `mini_sparkify_event_data.json`, consisting of \~128MB of data.
![](images\data_info.PNG)

## Data Cleaning

Before diving into analysis, we cleaned the dataset:

- **Invalid User IDs**: Removed rows with empty `userId` values, reducing the dataset from 286,500 to 278,154 rows.
- **Session IDs**: Verified `sessionId` for validity (none were missing).


### Resulting Dataset

After cleaning, we had 225 unique users with complete interaction logs for analysis.

![](images\churn_data.PNG)
---

## Exploratory Data Analysis (EDA)

### Defining Churn

Churn was defined using the `Cancellation Confirmation` page event:

#### Churn Distribution



- 23% of users churned (52 users).

### Behavioral Insights

#### User Listening Time

We calculated the average song length per user:

![](images\histograms_by_length.png)

**Observation**: Listening patterns between churned and non-churned users were similar, averaging 200–300 seconds. This could indicate that listening time alone might not be a strong predictor of churn, as it shows no significant distinction between the two groups. Further exploration into other behavioral factors could provide more clarity.

#### Gender Breakdown

![](images\gender_distribution.png)

**Observation**: Male users were more likely to churn than female users. This could suggest differences in engagement or satisfaction levels between genders. Exploring specific patterns or behaviors unique to male users, such as music preferences or frequency of interaction, might provide further insights.

#### User Level

![](images\level_distribution.png)

**Observation**: Free-tier users showed higher churn rates. This aligns with expectations, as free-tier users typically have less investment in the platform and may not feel as committed to continuing their subscription.

#### Membership Duration

![](images\membership_distribution.png)

**Observation**: Churned users often had memberships lasting fewer than 100 days. This observation suggests newer users are at higher risk of churn. Addressing this could involve improving the onboarding process, such as offering tailored recommendations, introductory tutorials, or exclusive incentives to increase early-stage engagement.

#### User Activity

![](images\avg_actions_distribution.png)
- **Actions per Session**: Churned users averaged fewer than 100 actions per session.

![](images\avg_artist_distribution.png)
- **Artists per Session**: Churned users engaged with fewer than 100 artists per session.

#### User Preferences

![](images\like_dislike.PNG)

- **Thumbs Up/Down**: Churned users gave fewer likes and dislikes.

![](images\add_friends_histogram.png)
![](images\histograms_add_to_playlist_by_churn.png)
- **Friend and Playlist Additions**: Minimal friend or playlist interactions were noted among churned users.

#### Operating System

![](images\os_distribution_pie.png)

**Observation**: MacOS and Windows dominated, but churn was OS-agnostic. This is an interesting observation. Do you think the OS distribution could influence other behaviors not related to churn?

---

## Feature Engineering

We engineered features to capture behavioral insights for machine learning models:

- **Songs Listened**: Total number of songs played.
- **Unique Artists**: Number of unique artists per user.
- **Thumbs Up/Down**: Total likes and dislikes.
- **Friend/Playlist Interactions**: Additions of friends or playlists.
- **Errors**: Frequency of error pages.
- **Membership Duration**: Days since user registration.
- **Device Type**: Derived from `userAgent`.
- **Churn**: Target label.

## Model Training

### Model Selection

We tested multiple models to identify the best-performing one:

1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Gradient Boosted Trees (GBT)**

### Training Process

- **Feature Assembly**: Features were vectorized for modeling.
- **Data Split**: 80% training and 20% testing.

### Random Forest Tuning

Random Forest emerged as the top performer. Hyperparameter tuning was applied to optimize:

- **Number of Trees**: Evaluated 50 and 100 trees.
- **Tree Depth**: Tested depths of 5 and 10.

## Results

### Model Performance

- **Best Model**: Random Forest achieved the highest accuracy and F1 score.

### Key Insights

- Behavioral signals like listening time, user level, and actions per session are strong churn predictors.
- Data-driven feature engineering improved model performance significantly.

---

## Conclusion

Conclusion
The Sparkify project highlights the power of combining EDA, feature engineering, and machine learning to predict user behavior. By understanding churn drivers, businesses can implement targeted retention strategies, ensuring higher user satisfaction and reduced attrition.

**Reflection**:

One of the most intriguing aspects of this project was the feature engineering process, particularly identifying and extracting behavioral signals such as membership duration and user engagement patterns. These insights not only enriched the dataset but also deepened our understanding of user behaviors. However, defining churn accurately presented significant challenges, as it required thoughtful consideration of event triggers and thresholds to ensure the model's relevance to real-world scenarios. These experiences underscore the critical balance between domain knowledge and technical expertise in solving data-driven problems.

**Improvement**:

While the project successfully predicted churn, one notable area for improvement is the model's generalizability to new user behaviors. The Random Forest Classifier, though highly effective, relies on feature representations that are static. This approach may struggle to adapt to evolving user patterns or platform changes over time.

A potential solution is to explore dynamic models like Recurrent Neural Networks (RNNs) or Transformer-based architectures, which can capture sequential patterns in user interactions. These models could incorporate time-series data to analyze trends in behavior over time, potentially providing deeper insights into churn risks. While these advanced methods might require more computational resources and careful hyperparameter tuning, they could significantly enhance the model's predictive capabilities compared to the current solution. Additionally, integrating external data sources, such as demographic or social media activity, might further enrich the analysis, enabling a more holistic understanding of user engagement.
