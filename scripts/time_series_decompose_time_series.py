import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("/Users/paramanandbhat/Downloads/5.2_decompose/data/train_data.csv")

train['Date'] = pd.to_datetime(train['Date'], format='%Y-%m-%d')
train.index = train['Date']

print(train.dtypes)

plt.figure(figsize=(12,8))

plt.plot(train.index, train['count'], label='Train')
plt.legend(loc='best')
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

decomposed_series = seasonal_decompose(train['count'],)


decomposed_series.plot()
plt.show()

(decomposed_series.seasonal[0:30]).plot()