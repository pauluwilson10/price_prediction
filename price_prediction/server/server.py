from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print(f"Locations: {locations}")
    response = jsonify({
        "locations": locations
    })
    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    print(f"Estimated Price: {estimated_price}")

    response = jsonify({
        'estimated_price': estimated_price
    })

    response.headers.add('Access-Control-Allow-Origin', "*")

    return response

if __name__ == "__main__":
    print("Starting Python Flask server for home price prediction")
    util.load_saved_artifacts()
    # print(f"Loaded locations: {util.get_location_names()}")
    app.run()
