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
    prediction = models['squat'].predict([data['features']])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict/bench', methods=['POST'])
def predict_bench():
    data = request.get_json()
    prediction = models['bench'].predict([data['features']])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict/deadlift', methods=['POST'])
def predict_deadlift():
    data = request.get_json()
    prediction = models['deadlift'].predict([data['features']])
    return jsonify({'prediction': prediction[0]})

@app.route('/predict/total', methods=['POST'])
def predict_total():
    data = request.get_json()
    prediction = models['total'].predict([data['features']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
