from .baseflatliner import BaseFlatliner

from influxdb import InfluxDBClient
import time

class InfluxdbStorage(BaseFlatliner):
    def __init__(self):
        super().__init__()


    def on_next(self, x):
        """ update l2 distance between cluster vector and baseline vector
        """
        client = InfluxDBClient(host='localhost', port=8086)
        client.switch_database('flatliner')
        client.write_points([{"measurement": "clusterdata",
        "tags": {
            "clusterID": x['cluster']
        },
        "fields": x}], time_precision='ms')