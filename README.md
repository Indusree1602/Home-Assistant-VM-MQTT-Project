 **Home Assistant – VM MQTT Project** 
MQTT IoT Sensor Integration with Home Assistant using Python

 **Student Details**
 Name:S Indu Sree  
 Register Number:42130187  
 MQTT Topic Used:home/indu-2025/sensor  
 Extra Sensor Implemented:Vibration Sensor  
 
 **Project Overview**
This project demonstrates an end-to-end integration of Python → MQTT → Home Assistant, 
where a Python script publishes IoT sensor data to an MQTT broker, and Home Assistant reads and displays those values in real time.

This assignment includes:
1. Installing **Home Assistant OS** on VirtualBox  
2. Installing and running **Mosquitto MQTT Broker**  
3. Writing a Python script to publish sensor data  
4. Configuring Home Assistant to subscribe and display the data  
5. Recording a demonstration video with timestamp and verification  
6. Uploading all materials to GitHub  

**Technologies Used**
- Home Assistant OS
- Mosquitto MQTT Broker
- Python 3
- Paho-MQTT library
- YAML configuration
- VirtualBox

 **MQTT Sensor Data Published**
The Python script publishes the following values:

- Temperature: 25°C  
- Humidity:60%  
- Vibration:1 (Custom sensor)  
- Student Name:S Indu Sree  
- Unique ID:42130187  
- MQTT Topic:home/indu-2025/sensor

**Python Script**
The script used for publishing MQTT messages is included in this repository:  
`mqtt_publish.py`
-It continuously sends JSON-formatted sensor data to the broker on port **1883**.

 **Home Assistant Configuration**
-The manually added MQTT sensors are defined in:  
`configuration.yaml`

Home Assistant reads:
- Indu Temperature  
- Indu Humidity  
- Indu Vibration  
- Indu Student Name  

All sensors were successfully displayed on the Home Assistant dashboard.

I also added Screenshots Included:
- Home Assistant Dashboard showing live sensor values  
- MQTT Logs  
- Python publishing output  

 **Assignment Video**
The project demonstration video includes:
- Face verification  
- Timestamp  
- Home Assistant interface  
- MQTT broker logs  
- Python script execution
  
**Conclusion**
This repository is part of the Nakshatra Automation Home Assistant Assignment, completed individually as required.  
All work in this project is original and configured by me(S INDU SREE).

 Files in This Repository
- `mqtt_publish.py` – Python publishing script  
- `configuration.yaml` – Home Assistant MQTT sensor configuration  
- `README.md` – Documentation  
- `Assignment.pdf` – Summary + screenshots  


