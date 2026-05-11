# Titanic Survival Prediction 🚢

## 📌 Project Overview

This project predicts whether a passenger survived the Titanic disaster using machine learning.

The Titanic dataset is one of the most popular datasets used to learn **classification algorithms, feature engineering, and model evaluation**.

In this project, multiple machine learning models were trained and compared to identify the best-performing model.

---

## 🎯 Problem Statement

Given passenger information such as:

* Age
* Sex
* Passenger Class
* Fare
* Embarkation Port

The goal is to build a machine learning model that predicts:

**Did the passenger survive?**

Target Variable:

* `Survived`

  * 0 → Did not survive
  * 1 → Survived

---

## 📂 Dataset

Dataset used: **Titanic Dataset**

Features used in the model:

* Pclass
* Sex
* Age
* SibSp
* Parch
* Fare
* Embarked

Dropped columns:

* PassengerId
* Name
* Ticket
* Cabin

---

## ⚙️ Machine Learning Workflow

The project follows a structured ML workflow:

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
15. Confusion Matrix
16. Model Saving

---

## 🤖 Models Trained

Five classification models were trained:

| Model                  | Accuracy |
| ---------------------- | -------- |
| Logistic Regression    | 81%      |
| K-Nearest Neighbors    | 81%      |
| Decision Tree          | 78%      |
| Random Forest          | 79%      |
| Support Vector Machine | **82%**  |

The **Support Vector Machine (SVM)** achieved the highest accuracy.

---

## 📊 Model Evaluation

The models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

  * Precision
  * Recall
  * F1 Score

---

## 🏆 Best Model

**Support Vector Machine (SVM)** performed best with an accuracy of **82%**.

The trained model was saved using **pickle** for future predictions.

---

## 💾 Saving the Model

The best model is stored as:

```
titanic_svm_model.pkl
```

This allows the model to be loaded later without retraining.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

---

## 📈 Key Concepts Practiced

This project covers important machine learning concepts:

* Data Cleaning
* Handling Missing Values
* Feature Encoding
* Feature Scaling
* Classification Algorithms
* Model Evaluation
* Confusion Matrix
* Classification Report
* Model Serialization

---

## 🚀 Future Improvements

Possible improvements for this project:

* Hyperparameter tuning
* Cross-validation
* Feature engineering
* Pipeline implementation

---

## 📚 Learning Outcome

By completing this project, you understand:

* End-to-end machine learning workflow
* Training multiple classification models
* Comparing model performance
* Saving trained models for deployment

---

## 👨‍💻 Author

Jitender
