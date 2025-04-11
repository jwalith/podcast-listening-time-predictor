# Podcast Listening Time Predictor 🎧

A Machine Learning project to predict how long users are likely to listen to a podcast episode based on episode features.
ML Projects	- Built and deployed a Machine Learning model using FastAPI to predict podcast listening time based on episode features; integrated a trained Random Forest pipeline with real-time prediction API; implemented API documentation using Swagger.
This project uses:
- **scikit-learn** to train the ML model
- **FastAPI** to build a lightweight backend API
- **Swagger UI** to test the API interactively

---

## Project Structure

```
podcast-listening-time-predictor/
│
├── model_training.ipynb        # ML model training notebook
├── final_model_pipeline.pkl    # Saved model pipeline (preprocessing + model)
├── app.py                      # FastAPI backend app
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## How to Run Locally 🚀

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/podcast-listening-time-predictor.git
cd podcast-listening-time-predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:

```bash
uvicorn app:app --reload
```

4. Open browser and visit:

```
http://127.0.0.1:8000/docs
```

✅ You can test the prediction API using the Swagger UI.

## Example API Usage

Send a POST request to `/predict` with JSON body:

```json
{
  "Episode_Length_minutes": 60.5,
  "Genre": "Comedy",
  "Host_Popularity_percentage": 70.0,
  "Publication_Day": "Monday",
  "Publication_Time": "Morning",
  "Guest_Popularity_percentage": 80.0,
  "Number_of_Ads": 2,
  "Episode_Sentiment": "Positive"
}
```

Response:

```json
{
  "predicted_listening_time_minutes": 42.02
}
```

