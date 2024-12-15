import joblib
import pandas as pd

modelA = joblib.load('models/random_forest_model_A.pkl')
modelC = joblib.load('models/random_forest_model_C.pkl')
modelD = joblib.load('models/random_forest_model_D.pkl')
modelHD = joblib.load('models/random_forest_model_HD.pkl')
encoded_columns = joblib.load('models/encoded_columns.pkl')

def predict_disease_risk(user_data):
    user_data_df = pd.DataFrame([user_data])
    user_data_encoded = pd.get_dummies(user_data_df, columns=['Exercise', 'Sex', 'Age_Category', 'Smoking_History', "Alcohol Consumption"])

    missing_cols = set(encoded_columns) - set(user_data_encoded)
    for col in missing_cols:
        user_data_encoded[col] = False

    user_data_encoded = user_data_encoded[encoded_columns]

    risk_percentage_A = modelA.predict_proba(user_data_encoded)[0][1] * 100
    risk_percentage_C = modelC.predict_proba(user_data_encoded)[0][1] * 100
    risk_percentage_D = modelD.predict_proba(user_data_encoded)[0][1] * 100
    risk_percentage_HD = modelHD.predict_proba(user_data_encoded)[0][1] * 100

    disease_risk = {
        'Arthritis': risk_percentage_A,
        'Cancer': risk_percentage_C,
        'Diabetes': risk_percentage_D,
        'Heart Disease': risk_percentage_HD
    }

    return disease_risk


    
    
   
