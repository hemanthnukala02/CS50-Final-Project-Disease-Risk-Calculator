import joblib
import pandas as pd

def predict_disease_risk(user_data):
    user_data_df = pd.DataFrame([user_data])
    user_data_encoded = pd.get_dummies(user_data_df, columns['Exercise', 'Sex', 'Age_Category', 'Height_(cm)', 'Weight_(kg)', 'Smoking_History', "Alcohol Consumption"])
    
    modelHD = joblib.load('models/random_forest_model_HD,pkl')
