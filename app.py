from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
MODEL_PATH = 'models/fraud_model.pkl'
SCALER_PATH = 'models/scaler.pkl'

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and Scaler loaded successfully.")
else:
    print("Error: Model or Scaler not found. Please run train_model.py first.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features (Time, V1...V28, Amount)
        # We'll expect 30 features from the user
        features = data['features']
        
        # Original columns: Time, V1...V28, Amount
        # Data processing script scaled Time and Amount
        
        df_input = pd.DataFrame([features], columns=[
            'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
            'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
            'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
        ])
        
        # Scale specific columns
        df_input[['Time', 'Amount']] = scaler.transform(df_input[['Time', 'Amount']])
        
        # Predict
        prediction = model.predict(df_input)[0]
        probability = model.predict_proba(df_input)[0][1]
        
        return jsonify({
            'status': 'success',
            'prediction': int(prediction),
            'probability': float(probability)
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(debug=True, host='0.0.0.0', port=port)
