import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle
data = pd.read_csv("D:\ppp\weatherdataset.csv")
data1=data[['maxtempC','mintempC','humidity','tempC', 'sunHour','HeatIndexC', 'pressure','windspeedKmph']]
y=data1["tempC"]
x=data1.drop(['tempC'], axis=1)
train_X, test_X, train_y, test_y = train_test_split(x,y,test_size=0.2)
regressor = DecisionTreeRegressor()
regressor.fit(train_X, train_y)
pickle.dump(regressor, open("model1.pkl", 'wb'))