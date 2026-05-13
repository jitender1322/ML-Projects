# 💳 Credit Card Fraud Detection

## 📌 Overview

Credit card fraud is one of the biggest challenges in the financial industry. Fraudulent transactions are extremely rare compared to normal transactions, making fraud detection a highly imbalanced classification problem.

This project focuses on building a Machine Learning model capable of detecting fraudulent credit card transactions using classification algorithms and imbalance handling techniques.

---

## 🎯 Objective

* Detect fraudulent transactions accurately
* Handle highly imbalanced data
* Compare multiple ML models
* Minimize false negatives
* Build a reliable fraud detection pipeline

---

## 🧠 Problem Type

* Supervised Learning
* Binary Classification

---

## 📊 Dataset Information

The dataset contains transactions made by European credit card holders.

### 📌 Features

* `Time` → Time elapsed between transactions
* `Amount` → Transaction amount
* `V1` to `V28` → PCA transformed numerical features
* `Class` → Target variable

### 🎯 Target Variable

| Class | Meaning                |
| ----- | ---------------------- |
| 0     | Normal Transaction     |
| 1     | Fraudulent Transaction |

---

## ⚠️ Dataset Challenge

This dataset is highly imbalanced:

* Normal Transactions → ~99.8%
* Fraud Transactions → ~0.2%

Because of this:

* Accuracy alone is not reliable
* Recall and F1-score become very important

---

## ⚙️ Project Workflow

1. Problem Statement
2. Import Libraries
3. Load Dataset
4. Data Understanding
5. Data Cleaning
6. Handle Missing Values
7. Encoding Categorical Features
8. Exploratory Data Analysis (EDA)
9. Feature / Target Split
10. Train-Test Split
11. Feature Scaling
12. Handle Imbalanced Data using SMOTE
13. Train Multiple Models
14. Model Evaluation
15. Model Comparison
16. Confusion Matrix
17. Save Best Model

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Pickle

---

## 🤖 Machine Learning Models Used

### 1. Logistic Regression

* Fast baseline model
* High recall but low precision

### 2. Decision Tree Classifier

* Captures nonlinear relationships
* Moderate performance

### 3. Random Forest Classifier

* Best-performing model
* Strong precision and recall balance

---

## ⚖️ Imbalanced Data Handling

This project uses:

# SMOTE (Synthetic Minority Oversampling Technique)

SMOTE generates synthetic fraud samples to balance the dataset and improve fraud detection capability.

---

## 📈 Evaluation Metrics

Because this is an imbalanced classification problem, the following metrics were used:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🏆 Model Performance

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.973    | 0.053     | 0.873  | 0.100    |
| Decision Tree       | 0.997    | 0.350     | 0.642  | 0.453    |
| Random Forest       | 0.999    | 0.911     | 0.758  | 0.828    |

---

## ✅ Best Model

### 🌲 Random Forest Classifier

Reasons:

* Highest F1-score
* Excellent precision
* Strong recall
* Best overall balance

---

## 🧮 Confusion Matrix

The confusion matrix was used to analyze:

* True Positives
* True Negatives
* False Positives
* False Negatives

Special focus was given to reducing:

# False Negatives

because undetected fraud can cause financial loss.

---

## 💾 Model Saving

The best-performing model was saved using:

```python
pickle
```

Saved file:

```text
fraud_detection_model.pkl
```

---

## 🚀 How to Run the Project

1. Download dataset from Kaggle
2. Install required libraries
3. Open Jupyter Notebook
4. Run all cells sequentially

---

## 📥 Dataset Source

Dataset:(https://drive.google.com/file/d/1_q7ea6BhrxgM5dodzPoR5ruaJZa2-dPP/view?usp=sharing
)
---

## 🔥 Key Learnings

This project helped in understanding:

* Imbalanced datasets
* SMOTE
* Fraud detection workflow
* Precision vs Recall
* Data leakage
* Feature scaling
* Model comparison
* Confusion matrix analysis

---

## 📌 Future Improvements

* Hyperparameter tuning
* XGBoost / LightGBM
* Real-time fraud detection API
* Model deployment with Flask/FastAPI
* Streamlit dashboard

---

## 👨‍💻 Author

Jitender
MERN Stack & Data Science Trainer
