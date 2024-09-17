from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Tải các mô hình từ các tệp .pkl
ridge_model = joblib.load('ridge_regression_model.pkl')
nn_model = joblib.load('neural_network_model.pkl')
lin_model = joblib.load('linear_regression_model.pkl')
@app.route('/')
def hello_world():
    return 'Bố mày đã deploy được rồi'
def extract_features(data):
    return np.array([
        data.get('cylinders', 0),
        data.get('displacement', 0),
        data.get('horsepower', 0),
        data.get('weight', 0),
        data.get('acceleration', 0),
        data.get('model_year', 0),
        data.get('origin', 0)
    ]).reshape(1, -1)

@app.route('/predict/ridge', methods=['POST'])
def predict_ridge():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    features = extract_features(data)
    ridge_pred = ridge_model.predict(features)[0]

    return jsonify({
        'result': ridge_pred
    })

@app.route('/predict/nn', methods=['POST'])
def predict_nn():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    features = extract_features(data)
    nn_pred = nn_model.predict(features)[0]

    return jsonify({
        'result': nn_pred
    })

@app.route('/predict/linear', methods=['POST'])
def predict_linear():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    features = extract_features(data)
    lin_pred = lin_model.predict(features)[0]

    return jsonify({
        'result': lin_pred
    })

if __name__ == '__main__':
    app.run(debug=True)
