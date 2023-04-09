from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import *
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import os

API_KEY = "b2765a91d67240b7b1d9d63e5831dd5d"
ENDPOINT = "https://memoria-anomalia.cognitiveservices.azure.com/"
DATA_PATH = "src/static/csv/request-data.csv"
client = AnomalyDetectorClient(ENDPOINT, AzureKeyCredential(API_KEY))

series = []
data_file = pd.read_csv(DATA_PATH, header=None, encoding='utf-8', date_parser=[0])
for index, row in data_file.iterrows():
    series.append(TimeSeriesPoint(timestamp=row[0], value=row[1]))

request = UnivariateDetectionOptions(series=series, granularity=TimeGranularity.DAILY)

change_point_response = client.detect_univariate_change_point(request)
anomaly_response = client.detect_univariate_entire_series(request)

for i in range(len(data_file.values)):
    if (change_point_response.is_change_point[i]):
        print("Change point detected at index: "+ str(i))
    elif (anomaly_response.is_anomaly[i]):
        print("Anomaly detected at index:      "+ str(i))
        print(data_file.values[i])