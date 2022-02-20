import json
import time
import random
import threading
import requests


class SensorData():
  """
  Class for Sensor Data
  """
  def __init__(self, user_id):
    """
    Constructor for Sensor Data class which generates random data for each key.
    """
    self.user_id = user_id
    self.timestamp = round(time.time())
    self.heart_rate = random.randint(40, 120) #considering only normal range of heart rate for humans
    self.respiration_rate = random.randint(12, 20), #considering only normal range of respiration rate for humans
    self.activity = random.randint(0, 10)


  def to_json(self):
    """
    Converting sensor data object into JSON format
    """
    data = {
        "user_id": self.user_id,
        "timestamp": self.timestamp,
        "heart_rate": self.heart_rate,
        "respiration_rate": self.respiration_rate,
        "activity": self.activity
    }

    return json.dumps(data)


class RepeatedTimer(object):
  """
  Class for Timer which creates a thread every second
  """
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False


def generate_sensor_data():
    """
    Function which generates new random data for "abc" user
    """
    sensor_data = SensorData("abc")
    sensor_data_json = sensor_data.to_json()

    res = requests.post(url="http://localhost:5000/vitals_input", data=sensor_data_json)
    return res


def start_simulator():
    """
    Function to start Simulator
    """
    rt = RepeatedTimer(1, generate_sensor_data)

if __name__ == "__main__":
    start_simulator()
