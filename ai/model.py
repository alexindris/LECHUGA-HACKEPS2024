import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

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

scaler_features = joblib.load('model/scaler_features.pkl')
scaler_target = joblib.load('model/scaler_target.pkl')

input_size = 5 
model = RegressionModel(input_size=input_size)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
checkpoint = torch.load('model/checkpoint_regression.pth', map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])
model.to(device)
model.eval()

def predict_cars_at_datetime(model, date_time_str):
    try:
        date_time = pd.to_datetime(date_time_str, format='%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date format. Please use the format 'YYYY-MM-DD HH:MM'.")
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

while True:
    date_time_input = input("Enter a date and time (YYYY-MM-DD HH:MM): ")
    predicted_cars = predict_cars_at_datetime(model, date_time_input)
    if predicted_cars is not None:
        roundValue = round(predicted_cars)
        print(f'Prediction: {roundValue}')
    else:
        print("Prediction error.")
