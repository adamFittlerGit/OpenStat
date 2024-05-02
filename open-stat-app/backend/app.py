from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

# Load the trained models
models = {
    'squat': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_squat.pkl'),
    'bench': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_bench.pkl'),
    'deadlift': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_deadlift.pkl'),
    'total': joblib.load('../../open-stat-ds/XGBoost/models/xgb_model_total.pkl')
}

@app.route('/predict/squat', methods=['POST'])
def predict_squat():
    data = request.get_json()
    features = data.get('features')
    # Parse features to the correct datatype
    Sex = 0 if features['Sex'] == 'F' else 1
    Age = float(features['Age'])
    Bodyweight = float(features['Bodyweight'])
    Squat_1 = float(features['Squat_1'])
    Squat_2 = float(features['Squat_2'])
    prediction = models['squat'].predict([[Sex, Age, Bodyweight, 1, Squat_1, Squat_2]])
    prediction_value = float(prediction[0])  # Convert to Python float
    return jsonify({'prediction': prediction_value})

@app.route('/predict/bench', methods=['POST'])
def predict_bench():
    data = request.get_json()
    features = data.get('features', {})
    prediction = models['bench'].predict([[features['Sex'], features['Age'], features['Bodyweight'], features['Equiptment'], features['Bench_1'], features['Bench_2']]])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict/deadlift', methods=['POST'])
def predict_deadlift():
    data = request.get_json()
    features = data.get('features', {})
    prediction = models['deadlift'].predict([[features['Sex'], features['Age'], features['Bodyweight'], features['Equiptment'], features['Deadlift_1'], features['Deadlift_2']]])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict/total', methods=['POST'])
def predict_total():
    data = request.get_json()
    prediction = models['total'].predict([data['features']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
