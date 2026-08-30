import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


read_csv = pd.read_csv('dataset/food_delivery_orders_dataset.csv')
read_csv = read_csv.dropna(subset=['actual_delivery_time_minutes'])
read_csv.columns =read_csv.columns.str.strip()
#print(read_csv.columns.tolist())

x =read_csv[
    [
        "distance_km",
        "traffic_level",
        "weather",
        "restaurant_preparation_time_minutes"
    ]]
y = read_csv["actual_delivery_time_minutes"]

x = pd.get_dummies(x,columns=['traffic_level', 'weather'])


print("NaN di X:", x.isnull().sum().sum())
print("NaN di y:", y.isnull().sum())

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

print('prediksi menit:', predictions)


