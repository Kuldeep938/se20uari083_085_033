# Raspberry Pi Real-Time Sensor Data Upload to Firebase

## Team Members
- Kuldeep Daram - SE20UARI083
- Sai Deep Reddy - SE20UARI085
- Bhargav Karra - SE20UARI033

## Experiment Details

In this project, we utilize a DHT11 Temperature and Humidity sensor for real-time data acquisition. Here are some key details about the sensor:

- **Measurement Range:** 0 - 50 Degrees
- **Humidity Error:** ±5%
- **Temperature Error:** ±2%
- **Power Supply:** 3.3v - 5v

## Raspberry pi connections with DHT11 sensor
  
  ![image](https://github.com/Kuldeep938/se20uari083_085_033/assets/84227754/513c601e-9de4-41c5-819d-fbc2abe6db60)

  ![image](https://github.com/Kuldeep938/se20uari083_085_033/assets/84227754/35593d98-bc9e-4ad7-bf67-29bc4a6b95a9)

-  PIN 1  3V3 with VCC
- PIN 6 GND with GND
- PIN 16 GPIO 23 with Data

After connecting the Raspberry Pi with a DHT11 sensor as described above, you can run the Raspi.py file on Raspberry Pi . This will automatically upload the sensor readings to the server. To view the sensor readings on your PC, run AI.py. It will display the values of temperature and humidity on your PC, with anomalies eliminated thanks to the applied Kalman filter.

## Use Case

### Smart Home Climate Control System

One practical use case of the DHT11 sensor is in a smart home climate control system. You can connect the DHT11 sensor to a microcontroller like Arduino or Raspberry Pi. Then, you can program the microcontroller to read temperature and humidity data from the sensor. The system can use this data to automatically control heating, ventilation, and air conditioning (HVAC) systems within the home. For instance, if the temperature becomes too high, the system can activate the air conditioner, and if humidity levels rise significantly, it can turn on a dehumidifier. This way, you can create a more comfortable and energy-efficient living environment.


## AI in project

Applying the Kalman filter to the sensor values to eliminate the anamolies in sensor readings.

### Working principle of the kalman filter:

The Kalman filter deals effectively with the uncertainty due to noisy sensor data and, to some extent, with random external factors. The Kalman filter produces an estimate of the state of the system as an average of the system's predicted state and of the new measurement using a weighted average. 










