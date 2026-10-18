from fastapi import FastAPI
from pydantic import BaseModel,Field
import joblib

app = FastAPI(title="Movie Sentiment Api")

model = joblib.load("./model/sentiment_model.pkl")
tfidf = joblib.load("./model/tfidf_vectorizer.pkl")

class SentimentRequest(BaseModel):
    text  : str = Field(min_length=1)


@app.post("/predict")
def predict_sentiment(request : SentimentRequest):

    review_text = request.text
    review_feature = tfidf.transform([review_text])

    prediction = model.predict(review_feature)
    pred_prob = model.predict_proba(review_feature)

    if prediction[0]==1:
        sentiment = "positive",
        confidence = pred_prob[0,1]*100
    else:
        sentiment = "negative",
        confidence = pred_prob[0,0]*100

    return {
        "sentiment" : sentiment,
        "confidence" : confidence
        }


