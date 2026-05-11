# House Price Prediction 🏠

## 📌 Project Overview

This project focuses on predicting house prices using machine learning regression algorithms.

House price prediction is an important problem in real estate analytics, helping buyers, sellers, and investors estimate property values based on house features.

In this project, multiple regression models were trained and evaluated to determine which algorithm performs best on the dataset.

---

## 🎯 Problem Statement

The objective of this project is to build a machine learning model that predicts the **price of a house** based on various features such as:

* Area of the house
* Number of bedrooms
* Number of bathrooms
* Number of stories
* Parking availability
* Furnishing status
* Other house attributes

Target Variable:

* `price`

The goal is to accurately estimate house prices using regression models.

---

## 📂 Dataset

Dataset used: **Housing Dataset**

Number of records: **545**

Features included in the dataset:

* `price`
* `area`
* `bedrooms`
* `bathrooms`
* `stories`
* `mainroad`
* `guestroom`
* `basement`
* `hotwaterheating`
* `airconditioning`
* `parking`
* `prefarea`
* `furnishingstatus`

---

## ⚙️ Machine Learning Workflow

The project followed a structured machine learning workflow:

1. Problem Understanding
2. Import Libraries
3. Load Dataset
4. Data Understanding
5. Data Cleaning
6. Handling Missing Values
7. Encoding Categorical Features
8. Exploratory Data Analysis (EDA)
9. Feature / Target Split
10. Train-Test Split
11. Feature Scaling
12. Model Training
13. Model Evaluation
14. Model Comparison
15. Model Saving

---

## 🔄 Data Preprocessing

### Handling Categorical Variables

Binary categorical variables such as:

* mainroad
* guestroom
* basement
* hotwaterheating
* airconditioning
* prefarea

were converted using **mapping (yes → 1, no → 0)**.

The `furnishingstatus` feature was encoded using **One-Hot Encoding**.

---

## 📊 Exploratory Data Analysis

EDA was performed to understand the relationships between variables.

A **correlation heatmap** was used to analyze how different features influence house prices.

Key observations:

* Area has strong influence on price
* Bathrooms and bedrooms also impact house value
* Some features have weaker correlations

---

## 🤖 Models Trained

Five regression models were trained and evaluated:

| Model                    | R² Score |
| ------------------------ | -------- |
| Linear Regression        | **0.65** |
| KNN Regressor            | 0.62     |
| Random Forest Regressor  | 0.61     |
| Decision Tree Regressor  | 0.47     |
| Support Vector Regressor | -0.10    |

---

## 📏 Evaluation Metrics

Since this is a regression problem, models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics measure how close the predicted prices are to the actual house prices.

---

## 🏆 Best Model

The **Linear Regression model** achieved the best performance with an **R² score of approximately 0.65**.

This indicates that the model explains about **65% of the variance in house prices**.

---

## 💾 Model Saving

The best model was saved using the **pickle library** so it can be reused later without retraining.

Saved file:

```id="fctc5q"
house_price_model.pkl
```

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

---

## 📚 Key Learnings

This project helped reinforce several important machine learning concepts:

* Difference between **classification and regression**
* Training multiple regression models
* Understanding **regression evaluation metrics**
* Comparing model performance
* Saving trained models for later use

One important insight from this project:

> A simple model with well-structured data can sometimes perform better than more complex models.

---

## 🚀 Future Improvements

Possible improvements for this project include:

* Feature engineering
* Adding location-based features
* Using cross-validation techniques
* Applying advanced ensemble models
* Building a deployment API for predictions

---

## 👨‍💻 Author

Jitender
