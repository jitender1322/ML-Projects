# 📉 Customer Churn Prediction

## 📌 Overview

Customer churn refers to when a customer stops doing business with a company. In highly competitive industries like telecom, predicting churn is crucial for retaining customers and improving business revenue.

This project focuses on building a Machine Learning model to predict whether a customer will churn based on historical data.

---

## 🎯 Objective

* Predict customer churn (Yes/No)
* Identify key factors affecting churn
* Help businesses take proactive retention actions

---

## 🧠 Problem Type

* Supervised Learning
* Binary Classification

---

## 📊 Dataset Description

The dataset contains customer information such as:

* Demographics (Gender, Senior Citizen, etc.)
* Account information (Tenure, Contract type)
* Services used (Internet, Phone, Streaming)
* Billing details (Monthly Charges, Total Charges)

### 🎯 Target Variable:

* `Churn`

  * Yes → Customer left
  * No → Customer stayed

---

## ⚙️ Project Workflow

1. Problem Understanding
2. Data Loading
3. Data Exploration
4. Data Cleaning
5. Handling Missing Values
6. Encoding Categorical Variables
7. Exploratory Data Analysis (EDA)
8. Feature Selection
9. Train-Test Split
10. Feature Scaling
11. Model Training
12. Model Evaluation
13. Model Comparison
14. Confusion Matrix
15. Model Saving

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🤖 Models Used

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors

---

## 📈 Evaluation Metrics

Since this is a classification problem, the following metrics were used:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🔍 Key Insights

* Customers with month-to-month contracts are more likely to churn
* Higher monthly charges increase churn probability
* Long-term customers are less likely to churn

---

## 💾 Model Saving

The best-performing model was saved using `joblib` for future predictions.

---

## 🚀 How to Run the Project

1. Clone the repository
2. Install dependencies
3. Open the Jupyter Notebook
4. Run all cells step-by-step

---

## 📌 Future Improvements

* Hyperparameter tuning
* Deployment using Flask / FastAPI
* Real-time prediction system

---

## 🙌 Conclusion

This project demonstrates how Machine Learning can help businesses reduce customer churn and improve retention strategies.

---

## 👨‍💻 Author

Jitender
MERN Stack & Data Science Trainer
