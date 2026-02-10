import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

print("Loading data...")
df = pd.read_csv('creditcard.csv')

# Feature scaling
print("Scaling features...")
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])
df['Time'] = scaler.fit_transform(df[['Time']])

# Split data
X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train model
print("Training Random Forest model (this may take a minute color)...")
# Using random_state for reproducibility and class_weight='balanced' to handle imbalance
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate
print("Evaluating model...")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model and scaler
print("Saving model and scaler...")
joblib.dump(model, 'models/fraud_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("Model and scaler saved in 'models/' directory.")
