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
squat_scl = joblib.load('../../open-stat-ds/XGBoost/scalers/scaler_squat.pkl')
bench_scl = joblib.load('../../open-stat-ds/XGBoost/scalers/scaler_bench.pkl')
dead_scl = joblib.load('../../open-stat-ds/XGBoost/scalers/scaler_deadlift.pkl')
total_scl = joblib.load('../../open-stat-ds/XGBoost/scalers/scaler_total.pkl')
sex_encoder = joblib.load('../../open-stat-ds/XGBoost/encoders/sex_encoder.pkl')
equipt_encoder = joblib.load('../../open-stat-ds/XGBoost/encoders/equipt_encoder.pkl')

@app.route('/predict/squat', methods=['POST'])
def predict_squat():
    # Get data and setup variables
    predictions = []
    data = request.get_json()
    f = data.get('features')
    n = int(data.get('number'))
    
    # Parse features to the correct datatype
    Sex = sex_encoder.transform(f['Sex'])
    Equiptment = equipt_encoder.transform(f['Equiptment'])
    Age = float(f['Age'])
    Bodyweight = float(f['Bodyweight'])
    Squat_1 = float(f['Squat_1'])
    Squat_2 = float(f['Squat_2'])
    
    features = np.array([[Sex, Age, Bodyweight, Equiptment, Squat_1, Squat_2]])
    
    for _ in range(n):
        # Scale the features using the StandardScaler
        scaled_features = squat_scl.transform(features)

        # Make a prediction using the XGBoost model
        result = models['squat'].predict(scaled_features)

        # Store the prediction
        predictions.append(float(result[0]))

        # Update the features array with the latest prediction
        features[0][-2] = features[0][-1]
        features[0][-1] = result[0]
        
    # I want to return the json in an easy way to append to the graph
    # I'll need to retrain all models and get the two unique label encoders
    return jsonify({'result': predictions})


@app.route('/predict/bench', methods=['POST'])
def predict_bench():
     # Get data and setup variables
    predictions = []
    data = request.get_json()
    f = data.get('features')
    n = int(data.get('number'))
    
    # Parse features to the correct datatype
    Sex = sex_encoder.transform(f['Sex'])
    Equiptment = equipt_encoder.transform(f['Equiptment'])
    Age = float(f['Age'])
    Bodyweight = float(f['Bodyweight'])
    Bench_1 = float(f['Bench_1'])
    Bench_2 = float(f['Bench_2'])
    
    features = np.array([[Sex, Age, Bodyweight, Equiptment, Bench_1, Bench_2]])
    #features = np.array([[1, 30, 90, 1, 255, 250]])
    
    for _ in range(n):
        # Scale the features using the StandardScaler
        scaled_features = bench_scl.transform(features)

        # Make a prediction using the XGBoost model
        result = models['bench'].predict(scaled_features)

        # Store the prediction
        predictions.append(float(result[0]))

        # Update the features array with the latest prediction
        features[0][-2] = features[0][-1]
        features[0][-1] = result[0]
        
    # I want to return the json in an easy way to append to the graph
    # I'll need to retrain all models and get the two unique label encoders
    return jsonify({'result': predictions})



@app.route('/predict/deadlift', methods=['POST'])
def predict_deadlift():
     # Get data and setup variables
    predictions = []
    data = request.get_json()
    f = data.get('features')
    n = int(data.get('number'))
    
    # Parse features to the correct datatype
    Sex = sex_encoder.transform(f['Sex'])
    Equiptment = equipt_encoder.transform(f['Equiptment'])
    Age = float(f['Age'])
    Bodyweight = float(f['Bodyweight'])
    Dead_1 = float(f['Deadlift_1'])
    Dead_2 = float(f['Deadlift_2'])
    
    features = np.array([[Sex, Age, Bodyweight, Equiptment, Dead_1, Dead_2]])
    
    for _ in range(n):
        # Scale the features using the StandardScaler
        scaled_features = dead_scl.transform(features)

        # Make a prediction using the XGBoost model
        result = models['deadlift'].predict(scaled_features)

        # Store the prediction
        predictions.append(float(result[0]))

        # Update the features array with the latest prediction
        features[0][-2] = features[0][-1]
        features[0][-1] = result[0]
        
    # I want to return the json in an easy way to append to the graph
    # I'll need to retrain all models and get the two unique label encoders
    return jsonify({'result': predictions})



@app.route('/predict/total', methods=['POST'])
def predict_total():
     # Get data and setup variables
    predictions = []
    data = request.get_json()
    f = data.get('features')
    n = int(data.get('number'))
    
    # Parse features to the correct datatype
    Sex = sex_encoder.transform(f['Sex'])
    Equiptment = equipt_encoder.transform(f['Equiptment'])
    Age = float(f['Age'])
    Bodyweight = float(f['Bodyweight'])
    Total_1 = float(f['Total_1'])
    Total_2 = float(f['Total_2'])
    
    features = np.array([[Sex, Age, Bodyweight, Equiptment, Total_1, Total_2]])
    
    for _ in range(n):
        # Scale the features using the StandardScaler
        scaled_features = total_scl.transform(features)

        # Make a prediction using the XGBoost model
        result = models['total'].predict(scaled_features)

        # Store the prediction
        predictions.append(float(result[0]))

        # Update the features array with the latest prediction
        features[0][-2] = features[0][-1]
        features[0][-1] = result[0]
        
    # I want to return the json in an easy way to append to the graph
    # I'll need to retrain all models and get the two unique label encoders
    return jsonify({'result': predictions})



if __name__ == '__main__':
    app.run(debug=True)
