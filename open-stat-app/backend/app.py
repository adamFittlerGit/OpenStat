from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained models
models = {
    'squat': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_squat.pkl'),
    'bench': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_bench.pkl'),
    'deadlift': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_deadlift.pkl'),
    'total': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_total.pkl')
}

# Load the trained scaler object
scaler = joblib.load('../../open-stat-ds/XGBoost/scalers/scaler_squat.pkl')
encoder = joblib.load('../../open-stat-ds/XGBoost/encoders/encoder_squat.pkl')
equiptment_encoder = joblib.load('../../open-stat-ds/XGBoost/encoders/encoder_squat.pkl')

@app.route('/predict/squat', methods=['POST'])
def predict_squat():
    data = request.get_json()
    features = data.get('features')
    # Parse features to the correct datatype
    Sex = encoder.transform(features['Sex'])
    Equiptment = encoder.transform(features['Equiptment'])
    Age = float(features['Age'])
    Bodyweight = float(features['Bodyweight'])
    Squat_1 = float(features['Squat_1'])
    Squat_2 = float(features['Squat_2'])
    
    features = np.array([[1, Age, Bodyweight, 1, Squat_1, Squat_2]])
    
    # Scale the input data
    scaled_features = scaler.transform(features)
    
    # Make the prediction
    prediction = models['squat'].predict(scaled_features)
    print(prediction)
    prediction_value = float(prediction[0])  # Convert to Python float
    return jsonify({'result': prediction_value})


@app.route('/predict/bench', methods=['POST'])
def predict_bench():
    data = request.get_json()
    features = data.get('features')
    # Parse features to the correct datatype
    Sex = encoder.transform(features['Sex'])
    Equiptment = encoder.transform(features['Equiptment'])
    Age = float(features['Age'])
    Bodyweight = float(features['Bodyweight'])
    Squat_1 = float(features['Bench_1'])
    Squat_2 = float(features['Bench_2'])
    
    # Scale the input data
    scaled_features = scaler.transform([[Sex, Age, Bodyweight, Equiptment, Squat_1, Squat_2]])
    
    # Make the prediction
    prediction = models['squat'].predict(scaled_features)
    prediction_value = float(prediction[0])  # Convert to Python float
    return jsonify({'prediction': prediction_value})

@app.route('/predict/deadlift', methods=['POST'])
def predict_deadlift():
    data = request.get_json()
    features = data.get('features')
    # Parse features to the correct datatype
    Sex = encoder.transform(features['Sex'])
    Equiptment = encoder.transform(features['Equiptment'])
    Age = float(features['Age'])
    Bodyweight = float(features['Bodyweight'])
    Squat_1 = float(features['Deadlift_1'])
    Squat_2 = float(features['Deadlift_2'])
    
    # Scale the input data
    scaled_features = scaler.transform([[Sex, Age, Bodyweight, Equiptment, Squat_1, Squat_2]])
    
    # Make the prediction
    prediction = models['squat'].predict(scaled_features)
    prediction_value = float(prediction[0])  # Convert to Python float
    return jsonify({'prediction': prediction_value})

@app.route('/predict/total', methods=['POST'])
def predict_total():
    data = request.get_json()
    features = data.get('features')
    # Parse features to the correct datatype
    Sex = encoder.transform(features['Sex'])
    Equiptment = encoder.transform(features['Equiptment'])
    Age = float(features['Age'])
    Bodyweight = float(features['Bodyweight'])
    Squat_1 = float(features['Total_1'])
    Squat_2 = float(features['Total_2'])
    
    # Scale the input data
    scaled_features = scaler.transform([[Sex, Age, Bodyweight, Equiptment, Squat_1, Squat_2]])
    
    # Make the prediction
    prediction = models['total'].predict(scaled_features)
    prediction_value = float(prediction[0])  # Convert to Python float
    return jsonify({'prediction': prediction_value})

if __name__ == '__main__':
    app.run(debug=True)
