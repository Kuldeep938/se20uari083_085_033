import pyrebase
from filterpy.kalman import KalmanFilter
import numpy as np

config = {
    "apiKey": "AIzaSyCb****5VIfJN******IF0Uv4udINwAfOlU",
    "authDomain": "rasp***y.firebaseapp.com",
    "databaseURL": "https://ra***r-***c-default-rtdb.fire**seio.com/",
    "storageBucket": "gs://ra****y-8d***c.ap**t.com/"}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def kalman_filter(sensor_data):
    # Create a Kalman filter
    kf = KalmanFilter(dim_x=2, dim_z=1)

    # Define initial state and covariance matrix
    kf.x = np.array([0., 0.])  # Initial state [position, velocity]
    kf.P *= 1e3  # Initial covariance matrix

    # Define state transition matrix (A) and measurement matrix (H)
    kf.F = np.array([[1., 1.], [0., 1.]])  # State transition matrix
    kf.H = np.array([[1., 0.]])  # Measurement matrix

    # Define process and measurement noise covariance matrices (Q and R)
    kf.Q *= 0.01  # Process noise covariance
    kf.R = 1.0  # Measurement noise covariance

    filtered_data = []

    # Update the filter for each sensor measurement
    for measurement in sensor_data:
        kf.predict()
        kf.update(measurement)
        filtered_data.append(kf.x[0])  # Extract the filtered position

    return filtered_data

# Fetch sensor data from Firebase
sensor_data = db.child('sensor_data').get().val()

# Apply the Kalman filter
filtered_data = kalman_filter(sensor_data)

print(filtered_data)
