import torch
import torch.nn as nn
import pandas as pd
import joblib  # type: ignore
import datetime
import numpy as np
from abc import ABC, abstractmethod

class RegressionModel(nn.Module):
    def __init__(self, input_size, hidden_size=64):
        super(RegressionModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size, 1)
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu1(out)
        out = self.fc2(out)
        out = self.relu2(out)
        out = self.fc3(out)
        return out

class PredictionService(ABC):
    @abstractmethod
    def predict_parking(self, date: datetime.datetime) -> int:
        raise NotImplementedError()


class ParkingPredictionService(PredictionService):
    def predict_parking(self, date: datetime.datetime) -> int:
        formatted_date = date.strftime('%Y-%m-%d %H:%M')
        scaler_features = joblib.load('infrastructure/service_locator/ai_model/scaler_features.pkl')
        scaler_target = joblib.load('infrastructure/service_locator/ai_model/scaler_target.pkl')

        input_size = 5 
        model = RegressionModel(input_size=input_size)

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        checkpoint = torch.load('infrastructure/service_locator/ai_model/checkpoint_regression.pth', map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])
        model.to(device)
        model.eval()
        predicted_cars = predict_cars_at_datetime(model, formatted_date,scaler_features,scaler_target,device)
        if predicted_cars is not None:
            roundValue = round(predicted_cars)
            return roundValue
        else:
            raise Exception("Prediction failed")

def predict_cars_at_datetime(model, date_time_str,scaler_features,scaler_target,device):
    try:
        date_time = pd.to_datetime(date_time_str, format='%Y-%m-%d %H:%M')
    except ValueError:
        return None
    
    features_input = {
        'Month': date_time.month,
        'Day': date_time.day,
        'DayOfWeek': date_time.dayofweek,
        'Hour': date_time.hour,
        'Minute': date_time.minute
    }
    
    df_input = pd.DataFrame([features_input])
    
    X_input = scaler_features.transform(df_input)
    
    X_input_tensor = torch.tensor(X_input).float().to(device)
    
    with torch.no_grad():
        prediction = model(X_input_tensor).cpu().numpy()
    
    prediction_descaled = scaler_target.inverse_transform(prediction.reshape(-1, 1))[0][0]
    
    return prediction_descaled
