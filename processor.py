import pandas as pd

CSV_PATH = "./static/csv/sensor_data.csv"


def store_in_csv(data):
    """
    Function to store sensor data in CSV file
    """

    # converting dict to dataframe
    new_sensor_data = pd.DataFrame(data, index=[0])

    #appending new sensor data to csv file
    new_sensor_data.to_csv(CSV_PATH, mode='a', index=False, header=False)


def get_report(interval):
    """
    Function to generated report based on interval
    """
    report = []
    interval = interval*60
    
    sensor_data = pd.read_csv(CSV_PATH)

    # calculating segement start for each record
    sensor_data['seg_start'] = sensor_data['timestamp'] - sensor_data['timestamp']%interval
    
    # calculating report fields for each interval
    for seg_start in sorted(sensor_data['seg_start'].unique()):
        df = sensor_data[sensor_data['seg_start'] == seg_start]
        data = {
                "user_id":sensor_data.loc[0, 'user_id'],
                "seg_start": int(seg_start),
                "seg_end": int(seg_start+interval),
                "avg_hr": int(df['heart_rate'].mean()),
                "min_hr": int(df['heart_rate'].min()),
                "max_hr": int(df['heart_rate'].max()),
                "avg_rr": int(df['respiration_rate'].mean())
            }
        report.append(data)

    return report
