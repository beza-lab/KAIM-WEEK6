from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained models
log_reg_model = joblib.load('log_reg_best_model.pkl')
rand_forest_model = joblib.load('rand_forest_best_model.pkl')

@app.route('/')
def home():
    return "Welcome to the ML Model Serving API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Extract features from the input data
    recency_bin = data['recency_bin']
    frequency_bin = data['frequency_bin']
    monetary_bin = data['monetary_bin']
    
    # Convert to numpy array for prediction
    features = np.array([[recency_bin, frequency_bin, monetary_bin]])
    
    # Predict with Logistic Regression
    log_reg_prediction = log_reg_model.predict(features)[0]
    log_reg_prob = log_reg_model.predict_proba(features)[0][1]
    
    # Predict with Random Forest
    rand_forest_prediction = rand_forest_model.predict(features)[0]
    rand_forest_prob = rand_forest_model.predict_proba(features)[0][1]
    
    # Create response
    response = {
        'log_reg_prediction': log_reg_prediction,
        'log_reg_probability': log_reg_prob,
        'rand_forest_prediction': rand_forest_prediction,
        'rand_forest_probability': rand_forest_prob
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)