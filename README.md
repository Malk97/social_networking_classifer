
# Social Network Ads Prediction API

This repository contains a machine learning-based API for predicting whether a user will purchase a product based on their demographic and salary details. The project includes data preprocessing, model training, and deployment using FastAPI and Docker.

## Docker Hub
To use the prebuilt Docker image, run:
```bash
docker pull malk37/social_network:latest
```

## Features
- Preprocess data using `pandas` and `scikit-learn`
- Train a classification model with XGBoost
- Deploy the model using FastAPI
- Dockerized for ease of deployment

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.11
- Docker
- Required Python libraries (listed in `requirements.txt`)

### Installation and Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/social_network_ads.git
   cd social_network_ads
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**:
   Run the script to preprocess the data, train the model, and save it:
   ```bash
   python train_model.py
   ```

4. **Run the FastAPI application**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Dockerize the application**:
   Build and run the Docker container:
   ```bash
   docker build -t social_network_ads .
   docker run -p 8000:8000 social_network_ads
   ```

6. **Pull the prebuilt Docker image**:
   Alternatively, pull the prebuilt image from Docker Hub:
   ```bash
   docker pull malk37/social_network:latest
   ```

## API Endpoints

### POST `/predict`
**Request Body**:
```json
{
  "Age": 30,
  "EstimatedSalary": 50000,
  "Gender": "Male"
}
```

**Response**:
```json
{
  "prediction": 1
}
```

- `prediction`: 1 indicates purchase, 0 indicates no purchase.



## Resources
- [Push a Docker Image to Docker Hub](https://www.youtube.com/watch?v=EIHY_CY5J0k)
- [Install Docker](https://www.youtube.com/watch?v=mS26N5cLBe8)
- [Deploy ML Model](https://www.youtube.com/watch?v=vA0C0k72-b4)
- [Docker Tutorial](https://youtu.be/JprTjTViaEA)

## Directory Structure
```
.
├── app
│   ├── main.py          # FastAPI application
│   └── requirements.txt # Python dependencies
├── Data
│   └── Social_Network_Ads.csv
├── xgb_model.json       # Trained XGBoost model
├── Dockerfile           # Docker configuration
├── train_model.py       # Script for training the model
└── README.md            # Project documentation
```
