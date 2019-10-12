import csv
import time
import luminol
from luminol.anomaly_detector import AnomalyDetector

bandwidth_up_timeseries = {}
with open('data/synthetic/tv.WAN.uncontrolled.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        bandwidth_up_timeseries[row[0]] = float(row[1])


bandwidth_up_detector = AnomalyDetector(bandwidth_up_timeseries,
                                        algorithm_name="bitmap_detector",
                                        score_threshold=10,
                                        algorithm_params={"precision":10})
anomalies = bandwidth_up_detector.get_anomalies()
for anomaly in anomalies:
    print(anomaly.start_timestamp, anomaly.end_timestamp, anomaly.anomaly_score)

