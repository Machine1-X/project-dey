import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

v = pd.read_csv('dataset you can get on this link "https://www.kaggle.com/datasets/mikhail1681/walmart-sales/data"')

v.columns = v.columns.str.strip()
v1 = v.select_dtypes(include=['str']).columns
## data prosesing 
"""cek data apakah ada yang str"""
#print(v.datatype)
"""cek apakah ada data yang nan"""
#print(v.isna().sum())
#print(v.isna().any().any())
#print("jumlah duplikat", v.duplicated().sum())
v['Date'] = pd.to_datetime(v['Date'], format = '%d-%m-%Y')
v= v.sort_values('Date')

v['Year'] = v['Date'].dt.year
v['Month'] = v['Date'].dt.month
v['day'] = v['Date'].dt.day
v['dayOfweek'] = v['Date'].dt.dayofweek
v =v.drop(columns=['Date'])
#print(v.dtypes)


model = LinearRegression()
model2 = RandomForestRegressor(n_estimators =200, random_state=42)

x = v.drop(columns=['Weekly_Sales'])
y = v['Weekly_Sales']

split_index = int(len(v)* 0.8)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)/ 
#you can replace this code to this code
"""x_train = x.iloc[:split_index]
x_test = x.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]"""

model.fit(x_train, y_train)
model2.fit(x_train, y_train)




prediksi = model.predict(x_test)
prediksi2 = model2.predict(x_test)

score = model.score(x_test, y_test)
score2 = model2.score(x_test, y_test)

mae = mean_absolute_error(y_test, prediksi2)
rmse = mean_squared_error(y_test, prediksi2) **0.5

print("prediksi penjualan mingguan model1:", prediksi)
print('skor modelmodel2:', score)
print("prediksi penjualan mingguan model 2", prediksi2)
print('skor model2: ', score2)
#print("MAE model2: ", mae)
#print("RMSE model2: ", rmse)
