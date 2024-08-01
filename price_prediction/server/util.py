import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts....start")
    global __data_columns
    global __locations
    global __model

    with open("C:\\Users\\Paulu wilson\\Desktop\\college\\machine_learning\\Real_life\\price_prediction\\server\\artifacts\\columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]  # Adjust this according to your columns.json structure

    with open("C:\\Users\\Paulu wilson\\Desktop\\college\\machine_learning\\Real_life\\price_prediction\\server\\artifacts\\banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading the artifacts are done...")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("kalhalli", 1000, 2, 2))
    print(get_estimated_price("Ejipura", 1000, 2, 2))

    