import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("/Users/paramanandbhat/Downloads/5.2_decompose/data/train_data.csv")

train['Date'] = pd.to_datetime(train['Date'], format='%Y-%m-%d')
train.index = train['Date']

print(train.dtypes)
