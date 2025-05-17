import pandas as pd 
import os
print("Current working directory:", os.getcwd())

# data ingestion 
df=pd.read_csv("weather_data_processing/raw_data/weather.csv")
df.info() # helps me to see how many null values are there in the dataset
