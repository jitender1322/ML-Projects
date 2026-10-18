# IMDb Movie Sentiment Analysis API

A machine learning project that classifies IMDb movie reviews as **positive or negative** using TF-IDF vectorization and Logistic Regression. The trained model is served through a REST API built with FastAPI, with Pydantic for request validation.

## Features

- Movie review sentiment classification
- TF-IDF text feature extraction
- Logistic Regression classification
- FastAPI REST API
- Pydantic request validation
- Interactive API documentation using Swagger UI
- Saved model and vectorizer for predictions without retraining

## Tech Stack

- Python
- Pandas
- scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- FastAPI
- Pydantic
- Uvicorn
- Joblib

## Project Structure

```text
Text_Sentiment_API/
├── main.py
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
├── data/                 # IMDb dataset (ignored by Git)
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/                # Virtual environment (ignored by Git)
```

## Dataset

This project uses the **IMDb Large Movie Review Dataset (`aclImdb`)**, containing 25,000 labeled training reviews and 25,000 labeled test reviews, along with additional unlabeled reviews.

### Download the dataset

- [Official Stanford dataset page](https://ai.stanford.edu/~amaas/data/sentiment/)
- [Direct dataset download — aclImdb_v1.tar.gz](https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz)

Download and extract the archive. Place the extracted `aclImdb` folder inside the project's `data/` directory.

Expected location:

```text
data/aclImdb/
```

The dataset is excluded from Git because of its size. Anyone reproducing this project can download it from the official source above.

## Installation and Setup

### 1. Clone the repository

Replace the placeholder with your repository URL.

```bash
git clone <your-repository-url>
cd Text_Sentiment_API
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Check the model files

Ensure the following files are available:

```text
model/sentiment_model.pkl
model/tfidf_vectorizer.pkl
```

The API requires both the trained model and the fitted TF-IDF vectorizer. If these files are not included in the repository, create them using your model training workflow.

### 5. Run the API

From the project root, run:

```bash
uvicorn main:app --reload
```

The API will start at:

`http://127.0.0.1:8000`

## API Usage

### Prediction endpoint

**Method:** `POST`

**Endpoint:** `/predict`

### Example request

```json
{
  "review": "This movie was absolutely fantastic and entertaining!"
}
```

### Example response

```json
{
  "review": "This movie was absolutely fantastic and entertaining!",
  "sentiment": "positive"
}
```

The response is illustrative; the actual prediction depends on the trained model.

## Interactive API Documentation

After starting the server, open:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Use Swagger UI to test the `/predict` endpoint by submitting your own movie reviews.

## How It Works

1. The client sends a movie review as JSON.
2. Pydantic validates the incoming request.
3. The fitted TF-IDF vectorizer transforms the review into numerical features.
4. The Logistic Regression model predicts the sentiment.
5. FastAPI returns the prediction as a JSON response.

## Important Notes

- The same fitted TF-IDF vectorizer used during model training must be used for prediction.
- The dataset is excluded from Git using the `data/` rule in `.gitignore`.
- The model and vectorizer must be available at the paths expected by the application.
- Only load trusted Joblib/pickle model files.

## Future Improvements

- Add automated API tests.
- Include prediction probabilities in the response.
- Add improved error handling and input validation.
- Develop a frontend for submitting reviews.
- Deploy the API to a cloud platform.

## Dataset Reference

Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). *Learning Word Vectors for Sentiment Analysis.*

Research paper: https://aclanthology.org/P11-1015/
