import joblib

# Load the trained model pipeline
model_pipeline = joblib.load('final_model_pipeline.pkl')


import pandas as pd
from pydantic import BaseModel

class PodcastFeatures(BaseModel):
    Episode_Length_minutes: float
    Genre: str
    Host_Popularity_percentage: float
    Publication_Day: str
    Publication_Time: str
    Guest_Popularity_percentage: float
    Number_of_Ads: int
    Episode_Sentiment: str

# Define the FastAPI app
from fastapi import FastAPI
app = FastAPI()
# Define the prediction endpoint
@app.post("/predict")
def predict_podcast(features: PodcastFeatures):
    # Convert the input features to a DataFrame
    input_data = features.dict()
    input_df = pd.DataFrame([input_data])
    
    # Make the prediction using the loaded model pipeline
    prediction = model_pipeline.predict(input_df)
    
    # Return the prediction result
    return {"predicted_listening_time_minutes": prediction.tolist()}

# Define Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Define Feedback Endpoint

class Feedback(BaseModel):
    user_feedback: str

@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    # For now, just print feedback (later you can save it to a file or database)
    print(f"Received feedback: {feedback.user_feedback}")
    return {"message": "Thank you for your feedback!"}