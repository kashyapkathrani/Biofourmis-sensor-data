# Biofourmis-sensor-data
Assignment for Boifourmis Interview

Steps to run the project:

1. Start Simulator - The simulator creates a new data which random values every second.

    > python simulator.py
    
2. Run Flask Application

    > flask run
    
    The two application contains two endpoints:
    1. /vitals_input (POST) : The endpoint stores the sensor data into CSV file. Simulator calls this endpoint after generting new data.
    
    ![Alt Text](https://github.com/kashyapkathrani/Biofourmis-sensor-data/blob/master/static/img/vitals_input.png)
    
    
    2. /vitals_output (GET) : The endpoint generates a report of sensor data based on the interval passed in as a query parameter.
    
    ![Alt Text](https://github.com/kashyapkathrani/Biofourmis-sensor-data/blob/master/static/img/vitals_output.png)
